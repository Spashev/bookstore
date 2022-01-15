from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User 
from django.http import HttpResponseRedirect
from .forms import RegisterForm


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login'
    template_name = 'home/home.html'


class RegisterView(TemplateView):
    template_name = 'account/register.html'
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login')
        else:
            return render(request, 'account/register.html')
