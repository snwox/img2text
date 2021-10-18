import numpy as np
import cv2
import os

from django.shortcuts import render
from django.http import HttpResponse
from base64 import b64decode
from PIL import Image
from django.conf import settings
import pytesseract
from pytesseract import *
# import time
# import cv2
# import numpy as np

def index(request):
	return render(request, 'index.html')

def action(request):
	data=request.POST['data']
	binary_data=b64decode(data[22:])
	print(settings.STATICFILES_DIRS)
	f=open(settings.STATICFILES_DIRS[0]+"/image.png","wb")
	f.write(binary_data)
	f.close()
	

	img = cv2.imread(settings.STATICFILES_DIRS[0]+'/image.png')
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(settings.STATICFILES_DIRS[0]+'/out.png',img_gray)

	text=pytesseract.image_to_string(Image.open(settings.STATICFILES_DIRS[0]+'/out.png'),lang="kor+eng")
	print(text)
	return render(request,'result.html',{"text":text})