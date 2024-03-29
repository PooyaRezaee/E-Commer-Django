from celery import shared_task
from .models import OtpCode
from datetime import timedelta

@shared_task
def auto_delete_otp():
    otp_codes = OtpCode.objects.all()
    for code in otp_codes:
        if code.is_expired():
            code.delete()