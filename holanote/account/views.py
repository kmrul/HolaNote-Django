from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User, Group

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text

from .forms import CreateUserForm, UserProfileForm
from .tokens import account_activation_token
from .decorators import unauthenticated_user

@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/dashboard')
        else:
            messages.warning(request, 'Username or password is incorrect')

    return render(request, 'templates/account/login.html')


@unauthenticated_user
def register(request):
    print('start registation')
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            

            ## send mail
            send_user_activation_mail(request, user)

            messages.success(request, 'Please confirm your email to complete registation')
            return redirect('register')
        else:
            print('form is not valid')

    context = {'form': form}
    return render(request, 'templates/account/register.html', context)



def forgot(request):
    return render(request, 'templates/account/forgot.html')


def reset(request):
    return render(request, 'templates/account/reset.html')

def logout(request):
    auth_logout(request)

    return redirect('login')

def profile(request):

    user_profile = request.user.profile
    form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')

    context = {
        'form':form
    }
    return render(request, 'templates/account/profile.html', context)


def activate(request, uidb64, token, *args, **kwargs):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as identifier:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        auth_login(request, user)
        messages.success(request, 'Your account have been confirmed')
        return redirect('home')
    else:
        messages.warning(request, 'Your confirmation link was invalid, possibly because it has already been used')
        return redirect('home')


def send_user_activation_mail(request, user):
    try:
        current_site = get_current_site(request)
        subject = 'Active your HolaNote account'
        message = render_to_string('templates/email/activation_email_template.html',
        {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        return user.email_user(subject, message)

        # template = render_to_string('templates/mail_template.html', {'name': request.user.username}) 
        # email = EmailMessage(
        #     'Thanks for sign up to kamruls website',
        #     template,
        #     'Kamrul Hasan',
        #     [form.cleaned_data.get('email')],
        # )
        # email.fail_silently = False
        # email.send()

    except Exception as e:
        return False



