import os

import requests
from django.core.exceptions import ValidationError


###Validation for POST admin form. Validate image existing.
def url_validator(url):
    try:
        image_request = requests.get(url)
    except:
        raise ValidationError('Bad URL!')

    if image_request.status_code == 200:
        image_path = os.getcwd() + '\\JBapi\\image_files\\' + url.split('/')[-1]
        out = open(image_path, "wb")
        out.write(image_request.content)
        out.close()
        return None
    else:
        return ValidationError('Bad URL!')
