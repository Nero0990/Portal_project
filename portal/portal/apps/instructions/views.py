
from django.http import HttpResponse

def instructions_view(request):
    return HttpResponse("Здесь скоро будут инструкции.")
