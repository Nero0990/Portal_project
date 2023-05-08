from django.http import HttpResponse

def question_view(request):
    return HttpResponse('Скоро здесь будут ответы на частые вопросы')