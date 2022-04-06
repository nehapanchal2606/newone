from django.urls import path
from . import views


urlpatterns = [
    path('show/', views.show),
    path('stu_login/', views.stu_login),
    path('degdet/<int:id>/', views.degdet),
    path('detail/<int:id>/', views.detail),
    path('fac/<int:id>/', views.fac),
    path('teacher/', views.teacher),
]