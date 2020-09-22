from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from  django.http import HttpResponse
from .forms import RegisterForm 
def home(request):
    return render(request,"base.html")


def register(request):

    if request.method == 'Post':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            teamname = form.cleaned_data.get('teamname')
            messages.success(request, f'Account created for { teamname }!')
            return redirect('base.html')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):

    return render(request, 'userlogin.html')