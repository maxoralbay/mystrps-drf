from django.core.management.base import BaseCommand
from datetime import date
from companies.models import Company, CompanyOwner, Office
from users.models import User


class Command(BaseCommand):
    help = "Seed the database with sample companies, offices, and owners"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=3,
            help="Number of companies to create (default: 3)",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing companies before seeding",
        )

    def handle(self, *args, **options):
        count = options["count"]
        clear = options["clear"]

        # Get or create admin user for company ownership
        admin_user, _ = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@example.com",
                "first_name": "Admin",
                "last_name": "User",
                "is_superuser": True,
                "is_staff": True,
            },
        )
        if not admin_user.check_password("admin123"):
            admin_user.set_password("admin123")
            admin_user.save()

        if clear:
            Office.objects.all().delete()
            CompanyOwner.objects.all().delete()
            Company.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Cleared existing companies, offices, and owners"))

        # Create sample companies
        companies_data = [
            {
                "name": "TechCorp Inc.",
                "legal_name": "TechCorp Incorporated",
                "company_code": "TECH001",
                "description": "Leading technology solutions provider",
                "industry": "Technology",
                "website_url": "https://techcorp.example.com",
                "foundation_date": date(2020, 1, 15),
            },
            {
                "name": "Global Services Ltd.",
                "legal_name": "Global Services Limited",
                "company_code": "GSERV001",
                "description": "International business services",
                "industry": "Services",
                "website_url": "https://globalserv.example.com",
                "foundation_date": date(2018, 6, 20),
            },
            {
                "name": "StartupXYZ",
                "legal_name": "StartupXYZ LLC",
                "company_code": "STXYZ001",
                "description": "Innovative startup company",
                "industry": "Innovation",
                "website_url": "https://startupxyz.example.com",
                "foundation_date": date(2022, 3, 10),
            },
        ]

        created_count = 0
        for i, company_data in enumerate(companies_data[:count]):
            company_code = company_data["company_code"]
            if not Company.objects.filter(company_code=company_code).exists():
                company = Company.objects.create(**company_data)
                created_count += 1

                # Create company owner
                CompanyOwner.objects.get_or_create(
                    company=company,
                    user=admin_user,
                    defaults={},
                )

                # Create main office
                Office.objects.get_or_create(
                    company=company,
                    name=f"{company.name} - Main Office",
                    defaults={
                        "address": f"123 Main Street, City {i+1}",
                        "is_main_office": True,
                        "is_active": True,
                    },
                )

                # Create additional office
                Office.objects.get_or_create(
                    company=company,
                    name=f"{company.name} - Branch Office",
                    defaults={
                        "address": f"456 Branch Avenue, City {i+1}",
                        "is_main_office": False,
                        "is_active": True,
                    },
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Created company: {company.name} (code: {company.company_code})")
                )

        # Create a child company (subsidiary)
        parent_company = Company.objects.first()
        if parent_company and not Company.objects.filter(company_code="TECH_SUB001").exists():
            child_company = Company.objects.create(
                name="TechCorp Subsidiary",
                legal_name="TechCorp Subsidiary Inc.",
                company_code="TECH_SUB001",
                description="Subsidiary of TechCorp Inc.",
                industry="Technology",
                tn_parent=parent_company,
            )
            CompanyOwner.objects.get_or_create(
                company=child_company,
                user=admin_user,
                defaults={},
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created child company: {child_company.name} (parent: {parent_company.name})"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeding complete! Created {created_count} companies. "
                f"Total companies: {Company.objects.count()}, "
                f"Total offices: {Office.objects.count()}, "
                f"Total owners: {CompanyOwner.objects.count()}"
            )
        )

