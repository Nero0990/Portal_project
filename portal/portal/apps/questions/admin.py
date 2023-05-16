from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'answer', 'instruction', 'topic')
    search_fields = ('text', 'answer', 'instruction__topic')

admin.site.register(Question, QuestionAdmin)