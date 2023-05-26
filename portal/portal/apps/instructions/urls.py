from django.urls import path
from . import views


urlpatterns = [
    path('', views.instructions_view, name='instructions'),
    path('<int:instruction_id>/', views.instruction_detail, name='instruction_detail'),
]
