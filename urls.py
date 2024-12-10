from django.urls import path, include

from . import views

# my application routes
urlpatterns = [
    path('', views.landing_page, name='home'),
    path('home', views.landing_page, name='home'),
    path('register', views.home, name='register'),
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/<str:pk>', views.student, name='student'),
]
