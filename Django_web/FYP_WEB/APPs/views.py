from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.http.response import StreamingHttpResponse

from django.contrib import messages
from .models import Entries, Exits
# upload files
from django.core.files.storage import FileSystemStorage

import os



from .camera import FaceRecognition
from .EntryTime import Entry
from .unauthorized_entry_detection import Unauthorized
from .ExitTime import Exit
from .camera import FaceRecognition

def camera(request):
    return render(request, 'Camera.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')



        user = auth.authenticate(username=username, password=password)

        if (username == 'santosh' and password=='1234'):


            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    else:


        return render(request, 'login.html')


def home(request):
    return render(request, 'Home.html')





def show_times(request):

    entry_data = Entries.objects.all()
    exit_data = Exits.objects.all()

    return render(request, 'ShowTimes.html', {'entry_data': entry_data, 'exit_data': exit_data})


def data_set(request):

    if request.method == 'POST':
        person_name = request.POST.get('Pname')
        person_position = request.POST.get('Position')

        dirname = f'{person_name}_{person_position}'

        os.mkdir('../../Images/Files/' + dirname)

        path_file = '../../Images/Files/' + dirname

        if request.FILES.get('document1', None):
            document_1 = request.FILES.get('document1')
            fs = FileSystemStorage(path_file)
            fs.save(document_1.name, document_1)

        #uploaded_file = request.FILES['document']

        if request.FILES.get('document2', None):
            document_2 = request.FILES.get('document2')
            fs = FileSystemStorage(path_file)
            fs.save(document_2.name, document_2)

        if request.FILES.get('document3', None):
            document_3 = request.FILES.get('document3')
            fs = FileSystemStorage(path_file)
            fs.save(document_3.name, document_3)
        messages.success(request, 'Upload Successful')
    return render(request, 'DataSet.html')





def gen(camera):
    while True:
        frame = camera.getFrame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def webcam_feed(request):
    '''Webcam feed'''
    return StreamingHttpResponse(gen(Exit()),
                                content_type='multipart/x-mixed-replace; boundary=frame')
