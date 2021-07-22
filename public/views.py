from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    if request.method != 'POST':
        return render(request, 'public/index.html')


def user_login(request):
    if request.method != 'POST':
        return render(request, 'public/authentication/login.html')
    else:
        phone = request.POST['phone']
        print('phone is '+phone)
        return redirect('public:user_login')


def user_reg(request):
    if request.method != 'POST':
        return render(request, 'public/authentication/register.html')
    else:
        return redirect('public:user_reg')


def forgot_pwd(request):
    if request.method != 'POST':
        return render(request, 'public/authentication/forgot_pwd.html')
