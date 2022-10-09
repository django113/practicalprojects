import os
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from .models import ProductImage


@receiver(pre_delete, sender=ProductImage)
def auto_image_delete_on_update(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding Product object files are updated.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
