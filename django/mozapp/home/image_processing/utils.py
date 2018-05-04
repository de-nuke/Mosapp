from django.core.files.base import ContentFile
from io import BytesIO
from .default_values_contants import *
import os.path
from PIL.Image import ANTIALIAS


def to_django_file(pil_image, name):
    img_io = BytesIO()
    extension = os.path.splitext(name)[1][1:]
    pil_image.save(img_io, format=extension.upper())
    return ContentFile(img_io.getvalue(), name=name)


def to_square(image, size):
    x = min(*image.size)
    ratio = size / x
    img = image.resize((int(image.size[0] * ratio), int(image.size[1] * ratio)), ANTIALIAS)

    center = (img.size[0] / 2, img.size[1] / 2)

    half_size = size / 2

    p1 = (int(center[0] - half_size), int(center[1] - half_size))
    p2 = (int(center[0] + half_size), int(center[1] + half_size))

    return img.crop(p1 + p2)


def resize(image, sizes, option):
    if option == SQUARE_TILE:
        assert sizes[0] == sizes[1]
        return to_square(image, sizes[0])
    if option == TILE_AS_MAIN_IMAGE:
        idx, val = min(enumerate(image.size), key=lambda x: x[1])
        ratio = sizes[idx] / val
        img = image.resize((int(image.size[0] * ratio), int(image.size[1] * ratio)), ANTIALIAS)

        center = (img.size[0] / 2, img.size[1] / 2)

        p1 = (int(center[0] - sizes[0] / 2), int(center[1] - sizes[1] / 2))
        p2 = (int(center[0] + sizes[0] / 2), int(center[1] + sizes[1] / 2))

        return img.crop(p1 + p2)
