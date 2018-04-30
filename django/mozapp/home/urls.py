from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    # path('image/', csrf_exempt(views.MainImageView.as_view()), name='image_upload'),
    path('image/', csrf_exempt(views.process_image), name='image_upload'),
]