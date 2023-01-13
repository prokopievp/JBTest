import os

import requests
from rest_framework import status


###Download image from url. path - ".../JBtest/JB/JBapi/image_files". 
###If image don't exists, response HTTP_400_BADREQUEST
def load_img(url, Response):
    try:
        image_request = requests.get(url)
    except:
        print('Bad image URL')
        return Response('Bad image URL', status=status.HTTP_400_BAD_REQUEST)
    if image_request.status_code == 200:
        image_path = os.getcwd() + '\\JBapi\\image_files\\' + url.split('/')[-1]
        out = open(image_path, "wb")
        out.write(image_request.content)
        out.close()
        return None
    else:
        print('Bad image URL')
        return Response('Bad image URL', status=status.HTTP_400_BAD_REQUEST)
