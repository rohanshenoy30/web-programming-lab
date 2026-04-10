from django.db import models

class Vote(models.Model):
    CHOICES = [
        ('good', 'Good'),
        ('satisfactory', 'Satisfactory'),
        ('bad', 'Bad'),
    ]

    choice = models.CharField(max_length=20, choices=CHOICES)