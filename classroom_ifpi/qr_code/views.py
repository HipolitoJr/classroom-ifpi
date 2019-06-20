# Create your views here.
import qrcode
from django.shortcuts import render
from django_qr_creator import Image


# def index(request):
#     link = [url='www.google.com']
#     return render(request, 'qr_code/qr_code.html', {'link': tuple(link)})


def index(request):
    link = "www.steampowered.com/dkufgiuyyyYY626537656fFfffhgftbOOBBOgfsSs"
    return render(request, 'qr_code/qr_code.html', {'link': link})
