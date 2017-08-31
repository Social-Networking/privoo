from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.views.generic.detail import DetailView

from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic.edit import UpdateView, CreateView

from .models import MyUser, Post
from .forms import LoginForm, SignupForm, EditForm


class WallView(LoginRequiredMixin, TemplateView):
    template_name = "wall.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created')
        return self.render_to_response(context)


class UserView(LoginRequiredMixin, DetailView):
    template_name = "user.html"
    model = MyUser

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(owner=self.object).order_by('-created')
        return context


class EditView(LoginRequiredMixin, UpdateView):
    template_name = "edit.html"
    form_class = EditForm
    success_url = "/"
    model = MyUser

    def get_object(self):
        return self.request.user


class LoginView(TemplateView):
    template_name = "login.html"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['login'] = LoginForm()
        context['signup'] = SignupForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        if request.GET.get('action') == "login":
            form_login = LoginForm(request.POST)

            if form_login.is_valid():
                user = authenticate(username=form_login.cleaned_data['email'], password=form_login.cleaned_data['password'])
                if user:
                    login(self.request, user)
                    return redirect("/")
                else:
                    messages.add_message(request, messages.INFO, _('Incorrect login data.'))

            context['login'] = form_login
        else:
            context['login'] = LoginForm()

        if request.GET.get('action') == "signup":
            form_signup = SignupForm(request.POST)
            if form_signup.is_valid():
                user = MyUser()
                user.is_active=False
                user.email = form_signup.cleaned_data['email']
                user.set_password(form_signup.cleaned_data['password'])
                user.save()
                messages.add_message(request, messages.INFO, _('Registered. Please activate account.'))
            context['signup'] = form_signup
        else:
            context['signup'] = SignupForm()

        return self.render_to_response(context)


class LogoutView(RedirectView):
    url = '/login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
