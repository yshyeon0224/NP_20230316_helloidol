from django.urls import path

from 뉴진스 import views

app_name = '뉴진스'

urlpatterns = [
    path('혜인/', views.show_혜인, name='혜인'),
    path('해린/', views.show_해린, name='해린'),
]