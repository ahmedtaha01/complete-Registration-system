from django.shortcuts import render
from django.shortcuts import render , redirect

from django.core.mail import EmailMessage 
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
import django
django.utils.encoding.force_text = force_str
from account.models import User

from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
# Create your views here.

def password_reset_request(request):
    if request.method == 'POST':
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    current_site = get_current_site(request)
                    email_template_name = "password/password_reset_email.html"
                    mail_subject = 'Activation link has been sent to your email id'
                    message = render_to_string(
                        email_template_name, {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': default_token_generator.make_token(user),
                            'email':user.email,
                            'site_name': 'Website',
                        }
                    )
                    email = EmailMessage(
                        mail_subject, message, to=[user.email]
                    )
                    email.send()
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})                    
   