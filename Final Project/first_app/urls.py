from django.urls import path
from first_app import views


app_name = 'first_app'
urlpatterns = [
    path(r'', views.index, name='OCRView'),
    path(r'search/', views.search, name='srch'),
]