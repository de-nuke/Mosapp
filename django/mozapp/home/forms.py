from django import forms
from .image_processing.default_values_contants import *


class ImageUploadForm(forms.Form):
    """Image upload form."""

    TILE_STYLE_CHOICES = [
        (SQUARE_TILE, 'Square tiles'),
        (TILE_AS_MAIN_IMAGE, 'Keep original image ratio')
    ]

    ENLARGEMENT_CHOICES = [
        (1, 'None'),
        (2, '2x'),
        (3, '3x'),
        (4, '4x'),
        (5, '5x'),
        (6, '6x'),
        (7, '7x'),
        (8, '8x'),
    ]

    image = forms.ImageField()
    name = forms.CharField(max_length=100, required=False, initial=DEFAULT_NAME)
    image_format = forms.ChoiceField(choices=[('png', 'PNG'), ('jpeg', 'JPEG')], required=False, initial='png')
    use_builtin_tile_images = forms.BooleanField(required=False, initial=USE_BUILTIN_TILE_IMAGES)
    apply_sepia = forms.BooleanField(required=False, initial=APPLY_SEPIA)
    apply_greyscale = forms.BooleanField(required=False, initial=APPLY_GREYSCALE)
    tile_style = forms.ChoiceField(choices=TILE_STYLE_CHOICES, required=False, initial=SQUARE_TILE)
    enlargement = forms.ChoiceField(choices=ENLARGEMENT_CHOICES, required=False, initial=DEFAULT_ENLARGEMENT)
    square_size = forms.IntegerField(required=False, max_value=100, initial=DEFAULT_SQUARE_TILE_SIZE)
    tiles_per_image_dimension = forms.IntegerField(required=False, max_value=1000, initial=DEFAULT_TILES_PER_IMAGE_DIMENSION)
    rows_number = forms.IntegerField(required=False)
    columns_number = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        optional_fields = [field[0] for field in self.fields.items() if not field[1].required]

        for field in optional_fields:
            if field not in self._submitted_fields:
                cleaned_data[field] = self.fields[field].initial
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ImageUploadForm, self).__init__(*args, **kwargs)
        self._submitted_fields = args[0].keys()
