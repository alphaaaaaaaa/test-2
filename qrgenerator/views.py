from django.shortcuts import render
import qrcode
import os
from io import BytesIO
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageDraw
import random
from django.http import JsonResponse
# Create your views here.
def generatorView(request):
    if request.GET.get('do') == 'true':
        url= request.GET.get('url')
        print(url)
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.make()
        img = qr.make_image()
        n = random.randint(0,9999)
        n = str(n)
        img.save(os.path.join(('qrgenerator/static/qr/test'+n+'.png')))
        image1 = Image.open('qrgenerator/static/cassette_papercraft.png')
        image2 = Image.open('qrgenerator/static/qr/test'+n+'.png')
    #resize, first image
        print('test')
        image1_size = image1.size
        image2 = image2.resize((200, 200))
        image2_size = image2.size

        new_image = Image.new('RGB',image1_size)
        new_image.paste(image1,(0,0))
        new_image.paste(image2,(320,340))
        new_image.save("qrgenerator/static/qr/test"+n+".png","JPEG")
        context = {
            'download':True,
            'file_name':'test'+n+'.png'
        }
        return JsonResponse(context)


    
    return render(request,'qrgenerator.html',{})
