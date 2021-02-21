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

def cit2020(request, cert_id):

    try:
        file_path = os.path.join(BASE_DIR, 'cit/data/cit2020/cit2020.csv')
        image_path = os.path.join(BASE_DIR, 'cit/data/cit2020/cit2020.png')
        font_path = os.path.join(BASE_DIR, 'cit/data/cit2020/ScriptMTBold.ttf')
        save_path = os.path.join(BASE_DIR, 'cit/data/cit2020/cit2020_all/')
        df = pd.read_csv(file_path)
        font = ImageFont.truetype(font_path, 140) 
        # font = ImageFont.truetype('arial.ttf', 90)
        font1 = ImageFont.truetype('arial.ttf', 45 )
        font2 = ImageFont.truetype('arial.ttf', 45)
        font3 = ImageFont.truetype('arial.ttf', 45)

        if(cert_id == "232696" or cert_id == "174630" or cert_id == "259682"):
            img_path = os.path.join(BASE_DIR, "cit/data/cit2020/" + cert_id + ".png")
            img = Image.open(img_path)
            draw = ImageDraw.Draw(img)
            draw.text(xy=(550, 1450), text='Certificate ID:', fill=(0, 0, 0), font=font1)                            #Certificate_Id
            draw.text(xy=(835, 1450), text= "CIT/20/" + cert_id, fill=(0, 0, 0), font=font1)
            
            
            draw.text(xy=(1230, 1450), text='Date:', fill=(0, 0, 0), font=font1)             #Date
            draw.text(xy=(1350, 1450), text='20/12/2020', fill=(0, 0, 0), font=font1)

            draw.text(xy=(800, 1530), text='Verify At:', fill=(0, 0, 0), font=font3)
            draw.text(xy=(1000, 1530), text='Istenitdgp.com/verify', fill=(0, 0, 0), font=font3)
            name = str(cert_id) + ".png"
            img_path = os.path.join(save_path, name)
            img.save(img_path)
            img = open(img_path, 'rb')
            response =HttpResponse(img, content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="ISTE_certificate.jpg"'
            return response

        for index,j in df.iterrows():
            if(int(cert_id) == int(j['SCNO'])):
                img = Image.open(image_path)
                draw = ImageDraw.Draw(img)
                
                if len(str([j['Name']])) > 15:
                    draw.text(xy=(780 - (len(str([j['Name']])) * 3 - 15), 710), text='{}'.format(j['Name']), fill=(0, 0, 0),font=font)
                elif len(str([j['Name']])) < 15:
                    draw.text(xy=(900 + (len(str([j['Name']])) * 3 - 15), 710), text='{}'.format(j['Name']), fill=(0, 0, 0),
                            font=font)
                
                draw.text(xy=(550, 1450), text='Certificate ID:', fill=(0, 0, 0), font=font1)                            #Certificate_Id
                draw.text(xy=(835, 1450), text='{}'.format("CIT/20/" + str(j['SCNO'])), fill=(0, 0, 0), font=font1)
                
                draw.text(xy=(1230, 1450), text='Date:', fill=(0, 0, 0), font=font1)             #Date
                draw.text(xy=(1350, 1450), text='20/12/2020', fill=(0, 0, 0), font=font1)

                draw.text(xy=(872, 910), text='{}'.format(j['College_Name']), fill=(0, 0, 0), font=font2)    #Student_OF
                
                draw.text(xy=(800, 1530), text='Verify At:', fill=(0, 0, 0), font=font3)
                draw.text(xy=(1000, 1530), text='Istenitdgp.com/verify', fill=(0, 0, 0), font=font3)
                
                name = str(j['SCNO']) + ".png"
                img_path = os.path.join(save_path, name)
                img.save(img_path)
                img = open(img_path, 'rb')

                response =HttpResponse(img, content_type='image/png')
                response['Content-Disposition'] = 'attachment; filename="ISTE_certificate.jpg"'

                return response

        return redirect(reverse_lazy('verifycert:invalid'))
    except:
        return redirect(reverse_lazy('verifycert:invalid'))