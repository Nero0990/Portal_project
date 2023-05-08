from django.http import HttpResponse

def home_view(request):
    return HttpResponse('Это главная страница нашего корпоративного портала.')