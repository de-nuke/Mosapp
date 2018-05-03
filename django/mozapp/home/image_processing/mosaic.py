from PIL import Image
import numpy as np

from django.core.files.storage import FileSystemStorage
import random
from .utils import to_django_file, resize
from .constants import *
from .effects import apply_effects


def get_builtin_images(images_dir, n=None):
    fs = FileSystemStorage()
    images = []

    file_list = fs.listdir(images_dir)[1]

    # Reduce number of input images if requested
    if n:
        while len(file_list) > n:
            file_list.pop(random.randrange(0, len(file_list)))

    for filename in file_list:
        img_path = fs.path('{}/{}'.format(images_dir, filename))
        try:
            images.append(Image.open(img_path))
        except IOError:
            print("Invalid file: {}. Skipping...".format(filename))
    return images


def get_user_images(img_pk_list=None):
    raise NotImplemented


def get_average_rgb(image):
    im = np.array(image)
    w, h, d = im.shape
    return tuple(np.average(im.reshape(w * h, d), axis=0))


def get_image_info(image):
    return {
        'image': image,
        'average_rgb': get_average_rgb(image)
    }


def split_image(image, dims, sizes):
    img_width, img_height = image.size
    tile_width = sizes[0]
    tile_height = sizes[1]
    col_num = dims[0]
    row_num = dims[1]

    new_image_width = col_num * tile_width
    new_image_height = row_num * tile_height
    org_img_center = (img_width / 2, img_height / 2)
    p1 = (int(org_img_center[0] - new_image_width / 2), int(org_img_center[1] - new_image_height / 2))
    p2 = (int(org_img_center[0] + new_image_width / 2), int(org_img_center[1] + new_image_height / 2))

    if new_image_width > img_width and new_image_height > img_height:
        image = image.crop(p1 + p2)

    imgs = []
    for i in range(row_num):
        for j in range(col_num):
            imgs.append(image.crop((j * tile_width, i * tile_height, (j + 1) * tile_width, (i + 1) * tile_height)))
    return imgs


def get_default_sizes(img, col_num, row_num, option=SQUARE_TILE):
    if option == SQUARE_TILE:
        if not col_num and not row_num:
            c = img.size[0] // DEFAULT_SQUARE_TILE_SIZE
            r = img.size[1] // DEFAULT_SQUARE_TILE_SIZE
            if img.size[0] % DEFAULT_SQUARE_TILE_SIZE:
                c += 1
            if img.size[1] % DEFAULT_SQUARE_TILE_SIZE:
                r += 1
            return (c, r), (DEFAULT_SQUARE_TILE_SIZE, DEFAULT_SQUARE_TILE_SIZE)
        elif not col_num and row_num:
            h = img.size[1] // row_num
            return (img.size[0] // h, row_num), (h, h)
        elif col_num and not row_num:
            w = img.size[0] // col_num
            return (col_num, img.size[1] // w), (w, w)
        else:
            return (col_num, row_num), (img.size[0] // col_num, img.size[1] // row_num)
    if option == TILE_AS_MAIN_IMAGE:
        if not col_num and not row_num:
            return ((TILES_PER_IMAGE_DIMENSION, TILES_PER_IMAGE_DIMENSION),
                    (img.size[0] // TILES_PER_IMAGE_DIMENSION, img.size[1] // TILES_PER_IMAGE_DIMENSION))
        elif not (col_num and row_num):
            return ((col_num or row_num, col_num or row_num),
                    (img.size[0] // (col_num or row_num), img.size[0] // (col_num or row_num)))
        else:
            return (col_num, row_num), (img.size[0] // col_num, img.size[1] // row_num)


def best_match(target_info, tile_infos):
    best = tile_infos[0]
    min_distance = float("inf")

    for tile_info in tile_infos:
        p1 = target_info['average_rgb']
        p2 = tile_info['average_rgb']

        distance = ((p2[0] - p1[0]) * (p2[0] - p1[0]) +
                    (p2[1] - p1[1]) * (p2[1] - p1[1]) +
                    (p2[2] - p1[2]) * (p2[2] - p1[2]))
        if distance < min_distance:
            min_distance = distance
            best = tile_info

    return best


def create_image_grid(images, dims, tile_size, output_size):
    width = tile_size[0]
    height = tile_size[1]

    col_num = dims[0]
    row_num = dims[1]

    assert col_num * row_num == len(images)
    assert output_size[0] == width * col_num
    assert output_size[1] == height * row_num

    grid_img = Image.new('RGB', output_size)

    for i in range(row_num):
        for j in range(col_num):
            grid_img.paste(images[j + i * col_num], (j * width, i * height))

    return grid_img


def create_mosaic(image, **kwargs):
    option = kwargs.get('tile_style', SQUARE_TILE)
    col_num = kwargs.get('columns_number', COLUMNS_NUMBER)
    row_num = kwargs.get('rows_number', ROWS_NUMBER)
    name = kwargs.get('name', NAME)
    image_format = kwargs.get('image_format', IMAGE_FORMAT)
    apply_greyscale = kwargs.get('apply_greyscale', APPLY_GREYSCALE)
    apply_sepia = kwargs.get('apply_sepia', APPLY_SEPIA)
    use_builtin_tile_images = kwargs.get('use_builtin_tile_images', USE_BUILTIN_TILE_IMAGES)

    img = Image.open(image)
    img = apply_effects(img, apply_sepia=apply_sepia, apply_greyscale=apply_greyscale)

    dims, sizes = get_default_sizes(img, col_num, row_num, option=option)

    target_images = split_image(img, dims, sizes)

    if use_builtin_tile_images:
        tile_images = get_builtin_images('tile_images', n=400)
    else:
        tile_images = get_user_images()

    for i in range(len(tile_images)):
        tile_images[i] = resize(tile_images[i], sizes, option=option)

    tile_images_infos = [get_image_info(img) for img in tile_images]
    target_images_infos = [get_image_info(img) for img in target_images]

    output_images = []
    for target_image_info in target_images_infos:
        best = best_match(target_image_info, tile_images_infos)
        output_images.append(best['image'])

    output_size = (dims[0] * sizes[0], dims[1] * sizes[1])
    mosaic_image = create_image_grid(output_images, dims, sizes, output_size)

    return to_django_file(mosaic_image, '{}.{}'.format(name, image_format))
