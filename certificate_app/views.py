from django.shortcuts import render,redirect
from .forms import CertificateForm
import cv2
from .models import Certificate
from django.core.files.base import ContentFile

from django.conf import settings
import os
# from django.views import generic

# Create your views here.

template_image = cv2.imread(os.path.join(settings.STATIC_ROOT,'death-certificate-template-36.png'))
# print(template_image)

def update_certificate_template(template_image, user_data):
    # Make a copy of the template to work on
    template = template_image.copy()
    zoom_factor = 0.5  # Example zoom factor of 0.5 (50% zoom out)

# Resize the image
    updated_template = cv2.resize(template, None, fx=zoom_factor, fy=zoom_factor)
    
    name_coords = (265,339)  
    location_coords = (305,462)  

    user_name = user_data['full_name']
    location = user_data['death_location']

    # Define the font, color, and size for the text to be added
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0, 0, 0)  # Black color (BGR format)
    font_scale = 1
    thickness = 2

    # Add the user's name and date to the updated_template
    cv2.putText(updated_template, user_name, name_coords, font, font_scale, color, thickness)
    cv2.putText(updated_template, location, location_coords, font, font_scale, color, thickness)

    return updated_template



def generate_certificate(request):
    form = CertificateForm
    updated_template = None
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            updated_template = update_certificate_template(template_image, user_data)
            ret,buf = cv2.imencode('.png',updated_template)
            image = ContentFile(buf.tobytes())
            certificate = Certificate(title=f"{user_data['full_name']}-{user_data['death_date']}")
            certificate.image.save(f"{user_data['full_name']}-{user_data['death_date']}.png", image)
            # certificate = Certificate.objects.create(title="sdhgfjhdghj",image=updated_template)
            certificate.save()
            return redirect('certificate_form')

    return render(request,'certificate_form.html',{'form':form,'updated_template':updated_template})





