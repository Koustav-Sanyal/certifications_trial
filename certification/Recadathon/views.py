from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import PIL
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
import base64
from django.http import FileResponse
from django.http import HttpResponse
from verifycert.forms import CertificateForm

# from django.core.servers.basehttp import FileWrapper
import mimetypes

def rd2020(request, cert_id):
    if(cert_id == "123456" or cert_id == "789456" or cert_id == "512456"):
        img_path = os.path.join(BASE_DIR, "rd/data/rd2020/" + cert_id + ".png")
        img = open(img_path, 'rb')
        response =HttpResponse(img, content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="ISTE_certificate.jpg"'
        return response    

    try:
        file_path = os.path.join(BASE_DIR, 'rd/data/rd2020/rd2020.csv')
        image_path = os.path.join(BASE_DIR, 'rd/data/rd2020/rd2020.png')
        save_path = os.path.join(BASE_DIR, 'rd/data/rd2020/rd2020_all/')
        df = pd.read_csv(file_path)
        font = ImageFont.truetype('arial.ttf',60)
        for index,j in df.iterrows():
            if(int(cert_id) == int(j['C_NO'])):
                img = Image.open(image_path)
                draw = ImageDraw.Draw(img)
                draw.text(xy=(250,350),text='{}'.format(j['name']),fill=(0,0,0),font=font)
                draw.text(xy=(400,200),text='{}'.format(j['C_NO']),fill=(0,0,0),font=font)
                name = j['name'] + ".png"
                img_path = os.path.join(save_path, name)
                img.save(img_path)
                img = open(img_path, 'rb')

                response =HttpResponse(img, content_type='image/png')
                response['Content-Disposition'] = 'attachment; filename="ISTE_certificate.jpg"'

                return response
                # response = FileResponse(img)
                # return response
        return redirect(reverse_lazy('verifycert:invalid'))
    except:
        return redirect(reverse_lazy('verifycert:invalid'))
