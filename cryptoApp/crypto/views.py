from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def SignupPage(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name, email, password)
    return render(request, 'signup.html')


def LoginPage(request):
    return render(request, 'login.html')
