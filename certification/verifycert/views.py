from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import CertificateForm
from .models import Certificate

def home(request):
    if request.method  == 'POST':
        form = CertificateForm(request.POST or None)
        
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, "verifycert/home.html", ctx)

        cert_num = form.cleaned_data.get('Certificate_Number')
        cert = Certificate.objects.all().filter(certificate_number = cert_num)
        if not cert:
            ctx = {'form' : form, 'valid': False}
            return render(request, "verifycert/home.html", ctx)
        else:
            return certificate(request, cert_num)

    else:
        form = CertificateForm(request.POST or None)
        ctx = {'form': form, 'valid':True}
        return render(request, "verifycert/home.html", ctx)

def certificate(request,cert_id):
    cert = Certificate.objects.all().filter(certificate_number = cert_id)
    if not cert:
        form = CertificateForm(request.POST or None)
        ctx = {'form' : form, 'valid': False}
        return render(request, "verifycert/home.html", ctx)
    else:
        ctx = {}
        return render(request, "verifycert/home.html", ctx)