import os

from django.utils import timezone
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):

    """

    File rename & repath

    Args:
        object: renamed path

    """

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        filename = filename.split(".")[0]
        today = timezone.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"{filename}_{today}.{ext}"
        return os.path.join(self.path, filename)

"""

Docs:

https://github.com/firdavsDev/ecommerce-mvt/blob/master/store/models/products.py

"""

"""

from store.path_rename import PathAndRename

product_thumbnail_path_and_rename = PathAndRename("products/thumbnails")
products_images_path_and_rename = PathAndRename("products/images")

thumbnail = models.ImageField(upload_to=product_thumbnail_path_and_rename, blank=True, null=True)

image = models.ImageField(upload_to=products_images_path_and_rename)

"""
