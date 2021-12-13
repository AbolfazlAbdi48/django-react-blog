from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

def validate_image(img):
    img_size = img.size
    max_upload_size = 2000000  # 2MB
    if img_size > max_upload_size:
        raise ValidationError("The image size is more than 2MB")
