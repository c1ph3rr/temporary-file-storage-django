import os
from django.shortcuts import render, redirect
from django.conf import settings

from .utils import slugify_filename, add_random_string
from .forms import StorageForm
from .models import StorageModel

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = StorageForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            slug = slugify_filename(file.name)
            slug = add_random_string(slug)
            file_path = os.path.join(settings.MEDIA_ROOT, slug)
            try:
                latest_id = StorageModel.objects.latest('file_id').file_id
            except:
                latest_id = 0
            url = f'download/{latest_id+1}/{slug}'
            model = StorageModel(file=file, file_path=file_path, url=url)
            model.save()
            return redirect('/')
    else:
        form = StorageForm()
    return render(request, 'tmp_app/index.html', {
        'form': form
    })


# def redirect(request):
#     pass