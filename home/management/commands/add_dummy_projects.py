from django.core.management.base import BaseCommand
from home.models import Project
from faker import Faker
import random


class Command(BaseCommand):
    help = "Adds 50 dummy projects to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        project_types = ["Client Project", "Internal Project"]
        statuses = ["ACTIVE", "COMPLETE"]

        for i in range(50):
            name = f"Project {fake.word().capitalize()} {i+1}"
            client = fake.company()
            start_date = fake.date_between(start_date="-2y", end_date="today")
            end_date = fake.date_between(start_date=start_date, end_date="+1y")
            project_type = random.choice(project_types)
            status = random.choice(statuses)

            Project.objects.create(
                name=name,
                client=client,
                start_date=start_date,
                end_date=end_date,
                type=project_type,
                status=status,
            )

        self.stdout.write(self.style.SUCCESS("Successfully added 50 dummy projects!"))
