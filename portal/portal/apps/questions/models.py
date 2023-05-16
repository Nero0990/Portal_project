from django.db import models
from instructions.models import Instruction

class Question(models.Model):
    text = models.TextField()
    answer = models.TextField()
    topic = models.CharField(max_length=255, choices=(
        ('Финансы', 'Финансы'),
        ('Продажи', 'Продажи'),
        ('Маркетинг', 'Маркетинг'),
    ))
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.text