import random
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.conf import settings
from .models import AppUser


def send_otp_via_mail(email, name):
    otp = random.randint(1000, 9999)
    
    otp_list = [int(digit) for digit in str(otp)]
    otp_content = {'name': name, 'otp': otp_list}
    email_from = settings.EMAIL_HOST
    html_template = 'user/otp_email.html'
    print(9)
    html_message = render(None, html_template, otp_content).content.decode()
    subject = "Confirm verification code"
    message = EmailMessage(subject, html_message, email_from, [email])
    print(10)
    message.content_subtype = 'html'
    print(7)
    message.send()
    print(8)
    user_obj = AppUser.objects.get(email=email) 
    user_obj.otp = otp 
    user_obj.save()


def send_registration_mail(email):
    subject = "your account verification email"
    otp = random.randint(1000,9999)
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    user_obj = AppUser.objects.get(email=email)
    user_obj.otp = otp 
    user_obj.save()