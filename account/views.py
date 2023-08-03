from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
import random
from django.core.mail import send_mail
from .models import UserOTP


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username=request.POST.get('username')
        name=request.POST.get('firstname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if not User.objects.filter(username=username).exists():
            if password1 == password2:
                User.objects.create_user(
                username=username,
                first_name=name,
                password=password1,
                email=email
                )
                messages.success(request,'Account created successfully')
                return redirect('login_user')
            else:
                messages.error(request,'password dosent\'t match !')
        else:
                messages.error(request,'username already exist')    
            
    return render(request,'register.html')  

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user= authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        messages.error(request,'Invalid username or password')    

    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')



def generate_otp():
    return str(random.randint(1000, 9999))

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'The given username does not exist!')
            return render(request, 'forgot.html')

        otp = generate_otp()
        send_mail(
            subject='Password reset',
            message=f'Here is your One-time password - {otp}',
            from_email='akashsa41066@gmail.com',
            recipient_list=[user.email],
            fail_silently=False
        )

        request.session['reset_user_id'] = user.id
        request.session['otp'] = otp
        return redirect('verify_otp', id=user.id)

    return render(request, 'forgot.html')

def verify_otp(request, id):
    user_id = request.session.get('reset_user_id')
    if user_id != id:
        return redirect('forgot_password')

    user = User.objects.get(id=id)
    submitted_otp = request.POST.get('otp')

    if request.method == 'POST' and submitted_otp == request.session.get('otp'):
        del request.session['otp']
        return redirect('password_change', id=user.id)
    else:
        messages.error(request, 'Invalid OTP!')
    return render(request, 'otp_verify.html', {'user': user})

def password_change(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user.set_password(password2)
            user.save()
            return redirect('user_login')
        else:
            messages.error(request, 'Passwords do not match!')
    return render(request, 'password_change.html')

