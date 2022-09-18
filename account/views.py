
from django.shortcuts import render ,redirect
from django.http import HttpResponse 
from django.contrib import messages
from .forms import RegisterForm
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
import django
django.utils.encoding.force_text = force_str
from .tokens import account_activation_token
from .models import User
from .forms import UserForm
from django.contrib.auth import authenticate, login



# Create your views here.

def socialHomeView(request):
    return redirect('/project')


# ////////////


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            ###################
            form.cleaned_data.get('username')
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string(
                'acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                }
            )
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

            # messages.success(request, 'Account was created for ' + user)
            # return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'registration/register.html', context)

    return render(request, 'registration/register.html', {})


def activate(request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')    


def signin(request):
    if request.method != "POST":
        form = UserForm()
        return render(request, 'registration/login.html', {'form': form})
    else:
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(
                request,
                username=username,
                password=password
        )
        if user is None:
            form = UserForm()
            return render(request, 'registration/login.html', {'form': form,'error':'invalid username or password'})
            # return HttpResponse("Invalid credentials.")
        login(request, user)
        return redirect('/project')


def home(request):
    return render(request,'home/home.html')


                     