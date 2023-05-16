from django.contrib import admin
from .models import Employee
from .models import Instruction

admin.site.register(Employee)

class InstructionAdmin(admin.ModelAdmin):
    list_display = ('topic', 'author', 'publish_date', 'file_link')
    search_fields = ('topic', 'author__fcs')

admin.site.register(Instruction, InstructionAdmin)