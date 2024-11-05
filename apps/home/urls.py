from django.urls import path
from apps.home import views
urlpatterns = [
    path('', views.index,name='home'),
    path('contact/', views.contact,name='contact'),
    path('appointment/', views.appointment,name='appointment'),
]