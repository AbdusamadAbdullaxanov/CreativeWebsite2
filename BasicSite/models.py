from django.db import models


class Model1(models.Model):
    SEVERAL_CHOICES = (
        ("1", "Junior"),
        ("2", "Middle"),
        ("3", "Senior"),
    )

    fullname = models.CharField(max_length=150, default='Unnamed User')
    age = models.IntegerField(max_length=9, blank=True, unique=False)
    email = models.EmailField(max_length=100, unique=True, blank=False, default=None)
    password = models.CharField(max_length=16, blank=False, unique=False, help_text=True)
    graduated = models.BooleanField(blank=True, default=True)
    reason = models.TextField(max_length=5000, default="Without description", blank=True, help_text=True)
    level = models.CharField(max_length=150, choices=SEVERAL_CHOICES, blank=False)

    def __str__(self):
        return self.fullname
