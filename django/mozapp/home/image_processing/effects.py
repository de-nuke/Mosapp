from PIL import Image
import numpy as np


def greyscale(image):
    pixels = image.load()
    for i in range(image.size[0]):  # for every col:
        for j in range(image.size[1]):  # For every row
            r, g, b = pixels[i, j]
            x = (r + g + b) // 3
            pixels[i, j] = (x, x, x)
    return image


def sepia(image):
    pixels = image.load()
    for i in range(image.size[0]):  # for every col:
        for j in range(image.size[1]):  # For every row
            r, g, b = pixels[i, j]

            new_r = min(round((r * 0.393) + (g * 0.769) + (b * 0.189)), 255)
            new_g = min(round((r * 0.349) + (g * 0.686) + (b * 0.168)), 255)
            new_b = min(round((r * 0.272) + (g * 0.534) + (b * 0.131)), 255)
            pixels[i, j] = (new_r, new_g, new_b)
    return image


def apply_effects(img, apply_sepia=False, apply_greyscale=False):
    image = img
    if apply_sepia:
        image = sepia(img)
    if apply_greyscale:
        image = greyscale(img)
    return image
