from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .forms import *
from .models import *
from .utils import send_otp_code
import random
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

__all__ = [
    'RegistretionUser',
    'VerifyCode',
    'LoginUserView',
    'LogoutView'
]


class RegistretionUser(View):
    form_class = UserRegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request,'You Logged',extra_tags='info')
            return redirect('home:index')

        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        context = {
            'form': self.form_class()
        }
        return render(request, 'account/register.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            full_name = data['full_name']
            phone_number = data['phone_number']
            email = data['email']
            password = data['password']
            print('='*10)
            code = random.randint(1000, 9999)
            print('='*10)
            OtpCode.objects.create(phone=phone_number, code=code)
            print('='*10)
            send_otp_code(phone_number, code)
            print('='*10)

            request.session['user_registration_info'] = {
                'full_name': full_name,
                'phone_number': phone_number,
                'email': email,
                'password': password,
            }
            print('='*10)

            messages.success(request,'Code Sended', extra_tags='info')
            return redirect('account:verify_code')
        else:
            messages.warning(request,'Form Not valid', extra_tags='warning')
            return render(request, 'account/register.html', {'form': form})



class VerifyCode(View):
    form_class = VerifyCodeForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request,'You Logged',extra_tags='info')
            return redirect('home:index')

        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        return render(request,'account/verify_code.html',{'form':self.form_class()})
    
    def post(self,request):
        form = self.form_class(request.POST)
        user_info = request.session['user_registration_info']
        if form.is_valid():
            cd = form.cleaned_data
            full_name = user_info['full_name']
            phone_number = user_info['phone_number']
            email = user_info['email']
            password = user_info['password']

            code_entered = cd['code']
            otp_obj = OtpCode.objects.filter(phone=phone_number).first()

            if otp_obj.check_code(code_entered):
                User.objects.create_user(phone_number=phone_number,email=email,full_name=full_name,password=password)
                otp_obj.delete()
                messages.success(request,'Your Account Created','success')
                return redirect('account:login')
            else:
                messages.error(request,'Code is Wrong','danger')
                return redirect('account:verify_code')



        else:
            messages.success(request,'form not valid',extra_tags='warning')
            return redirect('home:index')

class LoginUserView(View):
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request,'You Logged',extra_tags='info')
            return redirect('home:index')

        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        context = {
            'form': self.form_class()
        }
        return render(request, 'account/login.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            phone_number = data['phone_number']
            password = data['password']

            user = authenticate(request, phone_number=phone_number, password=password)
            print(phone_number)
            print(password)
            if user is not None:
                login(request,user)
                messages.success(request,'You Logged','success')
                return redirect('home:index')
            else:
                messages.error(request,'UserName or Password Is Wrong','danger')
                return redirect('account:login')

        else:
            messages.warning(request,'Form Not Valid','warning')
            return redirect('account:login')

class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You Logouted',extra_tags='info')
        return redirect('home:index')