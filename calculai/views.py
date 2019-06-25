import datetime
import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from calculai import models

path = os.path.join('/', 'home', 'pradhanmanva', 'UploadedMedia')


def index(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage(path)
        ext = file.name.split(".")[-1]
        if ext in ["jpg", "gif", "png", "jpeg", "tiff", "bmp", "ico"]:
            fs.save(file.name, file)
            file_metadata = models.Metadata()
            file_metadata.filename = file.name
            file_metadata.time = datetime.datetime.now()
            file_metadata.size = float(file.size) / 1000000
            file_metadata.save()
            return render(request, 'index.html', {"alert_message": "File Uploaded."})
        else:
            return render(request, 'index.html', {"alert_message": "Only Image Upload Allowed."})
    else:
        return render(request, 'index.html', {"alert_message": ""})


def list_file(request):
    documents = models.Metadata.objects.all()
    return render(request, 'list_file.html', {"data": documents})
