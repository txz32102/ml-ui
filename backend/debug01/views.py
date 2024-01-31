from django.shortcuts import render
from django.http import HttpResponse
from .forms import FileUploadForm

def file_upload_view(request):
    print('this is from post')
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            print(uploaded_file)
            return HttpResponse("File uploaded successfully")
    else:
        form = FileUploadForm()

    return render(request, 'debug01/upload.html', {'form': form})
