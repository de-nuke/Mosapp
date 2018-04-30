from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MainImageSerializer
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .forms import ImageUploadForm
from .image_processing import create_mosaic


class MainImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = (BasicAuthentication, )

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.FILES)
        image_serializer = MainImageSerializer(data=request.data)

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@require_http_methods(["POST"])
def process_image(request, *args, **kwargs):
    form = ImageUploadForm(request.POST, request.FILES or None)
    if form.is_valid():
        image = form.cleaned_data['image']
        apply_sepia = form.cleaned_data['apply_sepia']
        vertical_tiles_number = form.cleaned_data['vertical_tiles_number']
        result = create_mosaic(
            image=image,
            apply_sepia=apply_sepia,
            vertical_tiles_number=vertical_tiles_number
        )
        return JsonResponse({'git': 'gud'})
    else:
        print(form.errors)
        return JsonResponse(form.errors, status=400)
