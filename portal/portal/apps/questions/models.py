from django.db import models
from instructions.models import Instruction

class Question(models.Model):
    text = models.TextField(blank=True, null=True)
    answer = models.TextField( blank=True, null=True)
    topic = models.CharField(max_length=255, choices=(
        ('Финансы', 'Финансы'),
        ('Продажи', 'Продажи'),
        ('Маркетинг', 'Маркетинг'),
    ))
    instruction = models.ForeignKey(Instruction, on_delete=models.CASCADE, related_name='questions')

#выводим результаты с новой строки
    def __str__(self):
        return f'{self.text} {self.answer} {self.instruction}'