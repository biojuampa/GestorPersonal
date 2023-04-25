from django.db import models
from django.utils import timezone


class Priority(models.Model):
    level = models.CharField(max_length=20, unique=True, blank=True)

    def __str__(self):
        return self.level


class Task(models.Model):
    headline = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateField(default=timezone.now)
    deadline_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.headline

