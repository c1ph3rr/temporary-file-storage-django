import os
import re 
from datetime import timedelta
from django.utils import timezone
from django.utils.crypto import get_random_string


def slugify_filename(filename):
    name = str(filename).strip().replace(" ", "_")
    name = re.sub(r"(?u)[^-\w.]", "", name)
    return name


def default_expiry():
    return timezone.now() + timedelta(minutes=1)


# def add_random_string(name):
#     file, ext = os.path.splitext(name)
#     return '%s_%s%s' % (file, get_random_string(7), ext)


# def custom_path(file_id, filename):
#     return '{0}/{1}'.format(file_id, filename)