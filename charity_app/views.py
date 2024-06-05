from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.views import View
from charity_app.forms import AddDonationForm, UserRegistrationForm
from charity_app.models import Donation, Institution


class LandingPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('category')
        if category:
            context['institutions'] = Institution.objects.filter(category=category)
        else:
            context['institutions'] = Institution.objects.all()
        context['category'] = category
        return context



class AddDonationView(CreateView):
    model = Donation
    form_class = AddDonationForm
    template_name = 'form.html'


class DonationLoginView(LoginView):
    """Create login view using Django LoginView"""
    template_name = 'login.html'

    def form_valid(self, form):
        # User logged in
        return redirect('home')

    def form_invalid(self, form):
        return redirect('register')


class DonationLogoutView(LogoutView):
    next_page = 'home'


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']
            user.first_name = form.cleaned_data['name']
            user.last_name = form.cleaned_data['surname']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
        else:
            print(form.errors)
        return render(request, 'register.html', {'form': form})

        # if form.is_valid():
        #     form.save()
        #     return redirect('login')
        # return render(request, 'register.html', {'form': form})
