from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model

from sitemyfirst.settings import EMAIL_SERVER, EMAIL_ADMIN

from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import get_object_or_404

def send_contact_email_message(subject, email, content, ip, user_id):

    user = get_user_model().objects.get(id=user_id) if user_id else None
    message = render_to_string('women/feedback_email_send.html', {
        'email': email,
        'content': content,
        'ip': ip,
        'user': user,
    })
    email = EmailMessage(subject, message, EMAIL_SERVER, [EMAIL_ADMIN])
    email.send(fail_silently=False)

def send_activate_email_message(user_id):

    user = get_object_or_404(get_user_model(), id=user_id)
    #current_site = Site.objects.get_current().domain
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_url = f'users/confirm-email/{uid}/{token}/'
    subject = f'Активируйте свой аккаунт, {user.username}!'
    message = render_to_string('women/activate_email_send.html', {
        'user': user,
        'activation_url': f'http://localhost:8000/{activation_url}',
    })
    return user.email_user(subject, message)
