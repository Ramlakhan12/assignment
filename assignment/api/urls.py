from django.urls import path
from . import views  # Import your views from the current app

urlpatterns = [
    path('add-app/', views.add_app, name='add_app'),
    path('get-app/<int:id>/', views.get_app, name='get_app'),
    path('delete-app/<int:id>/', views.delete_app, name='delete_app'),
]