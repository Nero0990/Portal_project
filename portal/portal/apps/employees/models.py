from django.db import models

class Employee(models.Model):
    POSITION_CHOICES = (
        ('Исполнительный директор', 'Исполнительный директор'),
        ('Главный бухгалтер', 'Главный бухгалтер'),
        ('Генеральный директор', 'Генеральный директор'),
    )

    FCs = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    link = models.URLField(null=True, blank=False)

    def __str__(self):
        return self.FCs