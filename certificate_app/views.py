from django.shortcuts import render, redirect
from .forms import CertificateForm
from .models import DeathRecord
from django.core.files.base import ContentFile
from django.views import generic
from django.contrib.auth.decorators import login_required
from .certificate_generator import update_certificate_template
import cv2
import os
from django.conf import settings
from django.db.models import Q
from django.contrib import messages


# Create your views here.
template_image = cv2.imread(os.path.join(
    settings.STATIC_ROOT, 'death-certificate-template-36.png'))


class HomepageView(generic.TemplateView):
    template_name = 'homepage.html'


@login_required
def generate_certificate(request):
    form = CertificateForm
    updated_template = None
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            user_data = form.cleaned_data
            updated_template = update_certificate_template(
                template_image, user_data)
            ret, buf = cv2.imencode('.png', updated_template)
            image = ContentFile(buf.tobytes())
            certificate = DeathRecord(user=request.user, deceased_name=user_data['full_name'], evidence_of_death=user_data['evidence_of_death'],
                                      death_date=user_data['death_date'], date_of_birth=user_data['date_of_birth'], death_location=user_data['death_location'])
            certificate.image.save(
                f"{user_data['full_name']}-{user_data['death_date']}.png", image)
            certificate.save()
            messages.success(request,"You have successfully applied for Death Certificate")
            # return redirect('certificate_form')
            return redirect('certificate_detail', id=certificate.id)
        

    return render(request, 'certificate_form.html', {'form': form, 'updated_template': updated_template})


def search_records(request):
    query = request.GET.get('q')
    search_query = None
    if query:
        search_query = DeathRecord.objects.filter(deceased_name__iexact=query)

    return render(request,'search.html',{'search_query':search_query})

def certificate_detail(request, id):
    certificate = DeathRecord.objects.get(id=id)
    return render(request, 'certificate_detail.html', {'certificate':certificate})
