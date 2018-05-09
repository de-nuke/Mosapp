from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('image/<int:pk>/', csrf_exempt(views.get_image_url), name='get_image_url'),
    path('download/<int:pk>/', csrf_exempt(views.download_image), name='download_image'),
    path('image/', csrf_exempt(views.process_image), name='process_image'),
]