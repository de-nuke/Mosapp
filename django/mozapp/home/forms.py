from django import forms


class ImageUploadForm(forms.Form):
    """Image upload form."""

    TILE_STYLE_CHOICES = [
        (1, 'Square tiles'),
        (2, 'Keep original image ratio')
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
    use_builtin_tile_images = forms.BooleanField(required=False, initial=True)
    apply_sepia = forms.BooleanField(required=False, initial=False)
    apply_greyscale = forms.BooleanField(required=False, initial=False)
    tile_style = forms.ChoiceField(choices=TILE_STYLE_CHOICES, required=False, initial=1)
    enlargement = forms.ChoiceField(choices=ENLARGEMENT_CHOICES, required=False, initial=1)
    square_size = forms.IntegerField(required=False, max_value=100)
    rows_number = forms.IntegerField(required=False)
    columns_number = forms.IntegerField(required=False)

