from django.core.mail import send_mail
from django.conf import settings

def send_otp_code(email,name,code):
    send_mail(
        subject='Verify Code For core',
        message=f'Hello Dear {name},Tihs is Your Code {code}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email])

def send_custom_email(email,subject,message):
    send_mail(subject=subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[email])