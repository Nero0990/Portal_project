from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

def question_view(request):
    all_question = Question.objects.all()
    return render(request, 'questions.html', {'data' : all_question})

from .models import Question
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'questions/question_detail.html', {'question': question})