from django import forms


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
    use_builtin_tile_images = forms.BooleanField(required=False, initial=True)
    apply_sepia = forms.BooleanField(required=False, initial=False)
    apply_greyscale = forms.BooleanField(required=False, initial=False)
    vertical_tiles_number = forms.IntegerField(required=False)
    horizontal_tiles_number = forms.IntegerField(required=False)

