import os

from celery import shared_task
from django.core.mail import send_mail



@shared_task
def send_email_customer(name, email, phone, message):
    print('Sending message')
    msg = f'''
    {name}, {email}, {phone}, {message}  
    '''
    print(msg)
    send_mail(
        subject="Kun.uz",
        message=msg,
        from_email=os.getenv("EMAIL_HOST_USER"),
        recipient_list=[email],
        fail_silently=False,
    )



