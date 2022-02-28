import os
from django.core.exceptions import ValidationError


def validate_pdf_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_ext = ['.pdf']
    if not ext.lower() in valid_ext:
        raise ValidationError("Unsupported file extension")


def validate_video_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_ext = ['.mp4']
    if not ext.lower() in valid_ext:
        raise ValidationError("Unsupported file extension")
