from django.http import request
from django.shortcuts import render
import json
# Create your views here.
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User

class UsernamevalidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not username.isalnum():
            return JsonResponse({'username_error':'user name shoukd not contain alpha numeric'},status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error':'Sorry username exists choose another one'},status=409)
        return JsonResponse({'username':True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
