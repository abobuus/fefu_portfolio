from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import get_user_model

from users.forms import RegisterForm


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


class RegisterView(FormView):
    form_class = RegisterForm
    model = get_user_model()
    template_name = 'registration/register.html'
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


