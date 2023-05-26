from django.db import models
from employees.models import Employee

class Instruction(models.Model):
    topic = models.CharField(max_length=255)
    author = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='instructions')
    publish_date = models.DateField(auto_now_add=True)
    link = models.URLField(default="")
    file_link = models.URLField()

    def __str__(self):
        return f'{"Тема :", self.topic} {"Автор :",self.author} {"Дата :",self.publish_date} {"Ссылка :",self.link} {"Файл :",self.file_link}'
        