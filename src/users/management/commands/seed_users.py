from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "Seed the database with sample users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=5,
            help="Number of users to create (default: 5)",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing users before seeding",
        )

    def handle(self, *args, **options):
        count = options["count"]
        clear = options["clear"]

        if clear:
            User.objects.filter(is_superuser=False).delete()
            self.stdout.write(self.style.SUCCESS("Cleared existing users"))

        # Create superuser
        if not User.objects.filter(username="admin").exists():
            admin = User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123",
                first_name="Admin",
                last_name="User",
            )
            self.stdout.write(
                self.style.SUCCESS(f'Created superuser: {admin.username} (password: "admin123")')
            )

        # Create regular users
        created_count = 0
        for i in range(1, count + 1):
            username = f"user{i}"
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=f"user{i}@example.com",
                    password="password123",
                    first_name=f"User{i}",
                    last_name="Test",
                )
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created user: {user.username} (password: "password123")'
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeding complete! Created {created_count} new users. Total users: {User.objects.count()}"
            )
        )

