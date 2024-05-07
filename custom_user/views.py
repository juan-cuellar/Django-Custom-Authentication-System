#from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout as django_logout


from .models import CustomUser
from .forms import CustomUserForm, LoginForm


class Index(TemplateView):
    template_name = 'custom_user/index.html'


class Login(FormView):
    template_name = 'custom_user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/login/')

class Register(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = 'custom_user/register.html'
    success_url = reverse_lazy('login')