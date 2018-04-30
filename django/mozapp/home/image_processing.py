from PIL import Image
import numpy as np

from django.core.files.storage import FileSystemStorage


def get_builtin_images(images_dir):
    fs = FileSystemStorage()
    images = []
    for filename in fs.listdir(images_dir)[1]:
        img_path = fs.path('{}/{}'.format(images_dir, filename))
        try:
            images.append(Image.open(img_path))
        except IOError:
            print("Invalid file: {}. Skipping...".format(filename))
    return images


def get_user_images(img_pk_list=None):
    return []


def get_average_rgb(image):
    im = np.array(image)
    w, h, d = im.shape
    return tuple(np.average(im.reshape(w*h, d), axis=0))


def get_image_info(image):
    return {
        'average_rgb': get_average_rgb(image)
    }


def split_image(image, col_num, row_num):
    img_width, img_height = image.size
    tile_width = int(img_width / col_num)
    tile_height = int(img_height / row_num)

    imgs = []
    for i in range(row_num):
        for j in range(col_num):
            imgs.append(image.crop(j*tile_width, i*tile_height, (j+1)*tile_width, (i+1)*tile_height))
    return imgs


def get_default_sizes(img, col_num, row_num):
    if not col_num and not row_num:
        return int(img.size[1] / 20), int(img.size[0] / 20)
    elif not col_num and row_num:
        h = int(img.size[1] / row_num)
        return int(img.size[0] / h), row_num
    elif col_num and not row_num:
        w = int(img.size[0] / col_num)
        return col_num, int(img.size[1] / w)
    else:
        return col_num, row_num


def create_mosaic(image, apply_sepia=False, apply_greyscale=False, use_builtin_tile_images=True,
                  images_id=None, vertical_tiles_number=None, horizontal_tiles_number=None):
    if use_builtin_tile_images:
        tile_images = get_builtin_images('tile_images')
    else:
        tile_images = get_user_images()

    # Getting average RGB and <other information> about tile images
    infos = map(get_image_info, tile_images)
    print(list(infos))

    # Loading target image
    img = Image.open(image)
    if not horizontal_tiles_number or not vertical_tiles_number:
        col_num, row_num = get_default_sizes(img, horizontal_tiles_number, vertical_tiles_number)
    else:
        col_num, row_num = horizontal_tiles_number, vertical_tiles_number

    target_images = split_image(img, col_num=col_num, row_num=row_num)

    # TODO here: normalize tile images, so that they have the same based on the target_images sizes

    # TODO here: for each target image, find best matching tile using infos (store img in info ?)

    # TODO here: compose all fragments into one image

    # TODO here: apply sepia or greyscale

    # TODO here: return ready image with additional information (don't know what would be this information yet)

    return 0