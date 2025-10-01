from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import CustomUser


class SignUP(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        data = request.POST
        files = request.FILES

        username = data.get('username')
        email = data.get('email')
        phone_number = data.get('phone_number')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        gender = data.get('gender')
        image = files.get('image')
        bio = data.get('bio')
        birth_date = data.get('birth_date')
        password = data.get('password')
        repeat_password = data.get('repeat_password')

        if not all([username, email, phone_number, password, repeat_password]):
            messages.error(request, 'Please fill in all fields')
            return redirect('sign_up')

        if password != repeat_password:
            messages.error(request, 'Passwords do not match')
            return redirect('sign_up')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('sign_up')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('sign_up')

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            messages.error(request, 'Phone number already exists')
            return redirect('sign_up')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            image=image,
            bio=bio,
            birth_date=birth_date,
            password=password,
        )
        messages.success(request, 'User created successfully')
        login(request, user)
        return redirect('home')


class SignIN(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Incorrect username or password, Please try again')
            return redirect('sign_in')


@method_decorator(login_required, name='dispatch')
class SignOUT(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'User logged out successfully')
        return redirect('home')
