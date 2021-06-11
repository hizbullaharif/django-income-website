from django.http import request
from django.shortcuts import render, redirect
import json
# Create your views here.
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages, auth
from django.core.mail import EmailMessage
from django.contrib.auth import login,logout

class UsernamevalidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not username.isalnum():
            return JsonResponse({'username_error': 'user name shoukd not contain alpha numeric'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry username exists choose another one'}, status=409)
        return JsonResponse({'username': True})


class EmailvalidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is not valid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry email exists choose another one'}, status=409)
        return JsonResponse({'email': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.warning(request, "Password too short")
                    return render(request, 'authentication/register.html')
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                email_subject = "Activate your Acount"
                email_body = 'Testing'
                email = EmailMessage(
                    email_subject,
                    email_body,
                    'noreply@semcolon.com',
                    [email],

                )
                email.send(fail_silently=False)
                messages.success(request, "Acount created successfully")
        return render(request, 'authentication/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        if username and password:
            user = auth.authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    auth.login(request,user)
                    messages.success(request,"Logged in successfully")
                    return redirect('home')
        messages.error(request,"Fill username and password")
        return render(request, 'authentication/login.html')

class LogoutView(View):
    def post(self,request):
        auth.logout(request)
        messages.success(request,"You are successfully logged out")
        return redirect('login')

