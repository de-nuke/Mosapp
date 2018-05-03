from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .forms import ImageUploadForm
from .image_processing.mosaic import create_mosaic
from .models import MainImage


@require_http_methods(["POST"])
def process_image(request, *args, **kwargs):
    form = ImageUploadForm(request.POST, request.FILES or None)
    if form.is_valid():
        image = form.cleaned_data['image']
        apply_sepia = form.cleaned_data['apply_sepia']
        # vertical_tiles_number = form.cleaned_data['vertical_tiles_number']
        print('starting creating mosaic')
        # TODO: Pobieranie parametrów z requesta
        # TODO: 3 opcje: efekt na koniec, efekt na wejsciowy obraz i kafelki, efekt na wejsciowy obraz tylko
        # TODO: Enlargement - powiększanie obrazka, żeby kafelki były lepiej widoczne
        # TODO: KDTree.

        mosaic_image = create_mosaic(
            image=image,
        )
        print('finished mosaic')
        MainImage.objects.create(photo=mosaic_image)
        print('saved image to database')
        return JsonResponse({'git': 'gud'})
    else:
        print(form.errors)
        return JsonResponse(form.errors, status=400)
