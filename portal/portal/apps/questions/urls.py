from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_view, name='question'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
]