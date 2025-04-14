from django.db import models


class Project(models.Model):
    PROJECT_TYPES = [
        ("Client Project", "Client Project"),
        ("Internal Project", "Internal Project"),
    ]
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("COMPLETE", "Complete"),
    ]

    name = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    type = models.CharField(
        max_length=50, choices=PROJECT_TYPES, default="Client Project"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")

    def __str__(self):
        return self.name
