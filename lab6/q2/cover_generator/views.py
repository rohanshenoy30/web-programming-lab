from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import CoverForm

def index(request):
    cover_data = None
    if request.method == 'POST':
        form = CoverForm(request.POST, request.FILES)
        if form.is_valid():
            cover_data = form.cleaned_data
            if request.FILES.get('magazine_image'):
                image = request.FILES['magazine_image']
                fs = FileSystemStorage()
                filename = fs.save(image.name, image)
                cover_data['image_url'] = fs.url(filename)
    else:
        form = CoverForm()
    
    return render(request, 'index.html', {'form': form, 'cover_data': cover_data})
