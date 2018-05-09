from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .forms import ImageUploadForm
from .image_processing.mosaic import create_mosaic
from .models import MainImage
from django.shortcuts import get_object_or_404

@require_http_methods(["POST"])
def process_image(request, *args, **kwargs):
    form = ImageUploadForm(request.POST, request.FILES or None)
    if form.is_valid():
        # TODO: 3 opcje: efekt na koniec, efekt na wejsciowy obraz i kafelki, efekt na wejsciowy obraz tylko
        # TODO: Enlargement - powiększanie obrazka, żeby kafelki były lepiej widoczne
        # TODO: KDTree.

        mosaic_image = create_mosaic(**form.cleaned_data)
        obj = MainImage.objects.create(photo=mosaic_image)
        return JsonResponse({
            'pk': obj.pk,
        }, status=201)
    else:
        print(form.errors)
        return JsonResponse(form.errors, status=400)

@require_http_methods(["GET"])
def get_image_url(request, pk, *args, **kwargs):
    try:
        obj = MainImage.objects.get(pk=int(pk))
        url = request.build_absolute_uri(obj.photo.url)
        return JsonResponse({
            'pk': int(pk),
            'src': url,
        }, status=200)
    except MainImage.DoesNotExist:
        return JsonResponse({
            'status': 404,
            'message': "Image expired or doesn't exist"
        }, status=404)