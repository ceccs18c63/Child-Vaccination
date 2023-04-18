from django.shortcuts import render


# Create your views here.

def display(request):
    return render(request, 'index.html')


def display1(request):
    return render(request, 'login_all.html')


def display2(request):
    return render(request, 'login.html')


def display3(request):
    return render(request, 'hospital_register.html')


def display4(request):
    return render(request, 'patient_register.html')


def display5(request):
    return render(request, 'doctor_appoint.html')


def display6(request):
    return render(request, 'about.html')


def display7(request):
    return render(request, 'contact.html')
