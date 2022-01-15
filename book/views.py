from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


class MainView(TemplateView):
    template_name='home/main.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')