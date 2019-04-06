from django.shortcuts import render, reverse, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from .models import Provider
from requester.models import Requester
from provider.forms import RegistrationForm, LoginForm, ProviderForm
from django.views.generic import CreateView, FormView, DetailView, UpdateView, TemplateView, View, ListView
from requester import views as vi
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class Home(TemplateView):
    def get(self, request):
        return render(request, 'provider/home.html')

class Registration(CreateView):
    template_name = 'provider/register.html'
    form_class = RegistrationForm
    success_url = '/login/'

class Login(FormView):
    template_name = 'provider/login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        logout(request)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            sol = Provider.objects.filter(username=user).exists()
            req = Requester.objects.filter(username=user).exists()  
            if sol or req:
                return redirect(reverse('home'))
            return redirect(reverse('first_time'))
        return render(request, 'provider/login.html', {'form': form})

class CreateProvider(CreateView):
    model = Provider
    template_name = 'provider/provider.html'
    success_url = '/provider_profile/'
    fields = (
        'company_name',
        'address_line_1',
        'address_line_2',
        'city',
        'postal_code',
        'registration_no',
        'email_address',
        'website',
        'telephone',
        'logo',
        'description',
    )

    def form_valid(self, form):
        form.instance.username = self.request.user
        form.save()
        return super(CreateProvider, self).form_valid(form)

class ProviderProfile(TemplateView):
    model = Provider
    template_name = 'provider/provider_profile.html'

class ProviderUpdate(UpdateView):
    model = Provider
    success_url = '/provider_profile/'
    form_class = ProviderForm
    template_name = 'requester/provider_profile.html'

class FirstTime(TemplateView):
    def get(self, request):
        return render(request, 'provider/first_time.html')

class Providers(TemplateView):
    def get(self, request):
        return render(request, 'provider/providers.html')

class Accepted(TemplateView):
    def get(self, request, *args, **kwargs):
        view = vi.Challenges.as_view(
            template_name = 'provider/dashboard.html',
            paginate_by = 10
        )
        return view(request, *args, **kwargs)