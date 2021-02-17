from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import CertificateForm
from .models import Certificate
import PIL
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import base64
from django.http import FileResponse
from django.http import HttpResponse

# from django.core.servers.basehttp import FileWrapper
import mimetypes


def handler404(request, *args, **argv):
    return redirect(reverse_lazy('verifycert:invalid'))

def home(request):
    if request.method  == 'POST':
        form = CertificateForm(request.POST or None)
        
        if not form.is_valid() :
            print(form)
            ctx = {'form' : form, 'invalid':1}
            return render(request, "verifycert/home.html", ctx)

        cert_num = form.cleaned_data.get('Certificate_Number')
        return redirect(request.path + cert_num.lower())

    else:
        form = CertificateForm(request.POST or None)
        ctx = {'form': form, 'invalid': 0}
        return render(request, "verifycert/home.html", ctx)

def error(request,cert_id):
        return render(request, "verifycert/error.html", {})

def invalid(request):
        return render(request, "verifycert/error.html", {})

# def cit4_2020(request, cert_id):
#     file_path = os.path.join(BASE_DIR, 'verifycert/static/cit4_2020.csv')
#     image_path = os.path.join(BASE_DIR, 'verifycert/static/cit4_2020.jpeg')
#     save_path = os.path.join(BASE_DIR, 'verifycert/static/cit4_2020/')
#     df = pd.read_csv(file_path)
#     font = ImageFont.truetype('arial.ttf',60)
#     for index,j in df.iterrows():
#         if(int(cert_id) == int(j['C_NO'])):
#             img = Image.open(image_path)
#             draw = ImageDraw.Draw(img)
#             draw.text(xy=(250,350),text='{}'.format(j['name']),fill=(0,0,0),font=font)
#             draw.text(xy=(400,200),text='{}'.format(j['C_NO']),fill=(0,0,0),font=font)
#             name = j['name'] + ".jpg"
#             img_path = os.path.join(save_path, name)
#             img.save(img_path)
#             img = open(img_path, 'rb')

#             response =HttpResponse(img,content_type='image/jpg')
#             response['Content-Disposition'] = 'attachment; filename="cert.jpg"'

#             # wrapper      = FileWrapper(open(img_path))  # img.file returns full path to the image
#             # content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
#             # response     = HttpResponse(wrapper,content_type=content_type)  
#             # response['Content-Length']      = os.path.getsize(img_path)    
#             # response['Content-Disposition'] = attachment; filename=%s" %  name
#             return response
#             # response = FileResponse(img)
#             # return response

#     form = CertificateForm(request.POST or None)
#     ctx = {'form' : form, 'valid': False}
#     return render(request, "verifycert/home.html", ctx)
