import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .utils import slugify_filename
from .forms import StorageForm
from .models import StorageModel

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = StorageForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            model = StorageModel(file=file)
            model.save()

            model = StorageModel.objects.latest('file_id')
            slug = slugify_filename(model.file.name)
            file_path = os.path.join(settings.MEDIA_ROOT, slug)
            url = '{0}{1}'.format(settings.MEDIA_URL, slug)

            model.file_path = file_path
            model.url = url
            model.save(update_fields=['file_path', 'url'])

            return HttpResponseRedirect(reverse('redirect', kwargs={
                'file_id': model.file_id,
                'file_name': model.file
            }))
    else:
        form = StorageForm()
    return render(request, 'tmp_app/index.html', {
        'form': form
    })


def redirect(request, file_id, file_name):
    try:
        model = StorageModel.objects.get(file_id=file_id)
        return render(request, 'tmp_app/redirect.html', {
            'model': model
        })
    except StorageModel.DoesNotExist:
        raise Http404


#unique ids or unique names