from django.shortcuts import render

# Create your views here.
import os
from .models import ImgUpload
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
import json
from django.http.response import HttpResponse
from .forms import ImageForm

MEDIA_ROOT = settings.MEDIA_ROOT
COCO_ROOT = "/home/file/mmdetection/data/coco/test2017"
DETECT_ROOT = "/home/file/mmdetection/outs/img_results"

def upload_single(request):
    urls = []
    file_list = request.POST.get('file_list').split(',')
    print(file_list)

    for img in file_list:
        print(img)
        name = request.POST.get('name')
        new_img = ImgUpload(
            img=request.FILES.get(img),
            name=name
        )
        new_img.save()
        upload_name = new_img.img.name.split('/')[-1]
        print(upload_name)

        os.system("cp -f " + os.path.join(MEDIA_ROOT, 'img', upload_name) + ' ' + os.path.join(COCO_ROOT, upload_name))
        url = os.path.join('47.99.180.225:8080', 'MEDIA', 'outs', upload_name)
        urls.append(url)
    image_detection()

    print('urls  ', urls)

    response = JsonResponse(
        {
            'success': 'true',
            'url': urls
        }
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"

    return response


def image_detection():
    # images = IMG.objects.all()
    print("image detecting...")
    # os.system("cp -f " + os.path.join(COCO_ROOT, 'input.jpg') + ' ' + DETECT_ROOT)
    # os.system("python /home/file/mmdetection/tools/server_test.py")
    print("detection finished!")