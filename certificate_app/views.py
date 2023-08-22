from django.shortcuts import render,redirect
from .forms import CertificateForm
from .models import Certificate
from django.core.files.base import ContentFile
from django.views import generic
from django.contrib.auth.decorators import login_required
from .certificate_generator import update_certificate_template
import cv2
import os
from django.conf import settings

# Create your views here.
template_image = cv2.imread(os.path.join(settings.STATIC_ROOT,'death-certificate-template-36.png'))


class HomepageView(generic.TemplateView):
    template_name = 'homepage.html'
    


@login_required
def generate_certificate(request):
    form = CertificateForm
    updated_template = None
    if request.method == 'POST':
        form = CertificateForm(request.POST,request.FILES)
        if form.is_valid():
            user_data = form.cleaned_data
            updated_template = update_certificate_template(template_image, user_data)
            ret,buf = cv2.imencode('.png',updated_template)
            image = ContentFile(buf.tobytes())
            certificate = Certificate(user=request.user,title=f"{user_data['full_name']}-{user_data['death_date']}",evidence_of_death=user_data['evidence_of_death'])
            certificate.image.save(f"{user_data['full_name']}-{user_data['death_date']}.png", image)
            certificate.save()
            return redirect('certificate_form')

    return render(request,'certificate_form.html',{'form':form,'updated_template':updated_template})





