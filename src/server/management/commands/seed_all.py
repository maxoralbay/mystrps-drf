from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Seed all modules with sample data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing data before seeding",
        )
        parser.add_argument(
            "--users",
            type=int,
            default=5,
            help="Number of users to create (default: 5)",
        )
        parser.add_argument(
            "--companies",
            type=int,
            default=3,
            help="Number of companies to create (default: 3)",
        )

    def handle(self, *args, **options):
        clear = options["clear"]
        users_count = options["users"]
        companies_count = options["companies"]

        self.stdout.write(self.style.WARNING("Starting database seeding..."))

        # Seed users
        self.stdout.write(self.style.SUCCESS("\n=== Seeding Users ==="))
        call_command("seed_users", count=users_count, clear=clear)

        # Seed companies
        self.stdout.write(self.style.SUCCESS("\n=== Seeding Companies ==="))
        call_command("seed_companies", count=companies_count, clear=clear)

        self.stdout.write(self.style.SUCCESS("\n=== All seeding complete! ==="))
        self.stdout.write(
            self.style.SUCCESS(
                "\nYou can now login with:\n"
                "  - Username: admin, Password: admin123\n"
                "  - Username: user1, Password: password123\n"
                "  - Username: user2, Password: password123\n"
                "  - etc...\n"
            )
        )

