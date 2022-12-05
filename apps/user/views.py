from django.shortcuts import render
from django.views import View
from django.views.generic import UpdateView,CreateView,ListView,DetailView,DeleteView
from apps.account.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import Address
from django.contrib import messages

__all__ = [
    'ProfileView',
    'AddressesView',
    'DeleteAddressView',
    'CreateAddresView',
    'OredersView',
    'OrederDetailView',
]

class ProfileView(LoginRequiredMixin,UpdateView):
    template_name = 'user/profile.html'
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('user:profile')

    def get_object(self):
        return User.objects.get(id=self.request.user.id)

class AddressesView(LoginRequiredMixin,ListView):
    template_name = 'user/addresses.html'
    context_object_name = 'addresses'

    def get_queryset(self):
        addresses = Address.objects.filter(to=self.request.user)

        return addresses

class DeleteAddressView(LoginRequiredMixin,DeleteView):
    model = Address
    success_url = reverse_lazy('user:addresses')
    template_name = 'user/delete_address.html'

    def form_valid(self, form):
        messages.success(self.request,'Address Deleted',extra_tags='info')
        return super().form_valid(form)


class CreateAddresView(LoginRequiredMixin,CreateView):
    model = Address
    form_class = UserCreateAddressForm
    template_name = 'user/create_address.html'
    success_url = reverse_lazy('user:addresses')

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.to = self.request.user

        return super().form_valid(form)

class OredersView(LoginRequiredMixin,ListView):
    pass

class OrederDetailView(LoginRequiredMixin,DetailView):
    pass