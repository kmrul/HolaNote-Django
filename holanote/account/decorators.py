from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(requst, *args, **kwagrs):
        if requst.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(requst, *args, **kwagrs)

    return wrapper_func

def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(requst, *args, **kwagrs):
            return view_func(requst, *args, **kwagrs)
        return wrapper_func

    return decorator

def admin_only(view_func):
    def wrapper_func(requst, *args, **kwagrs):
        group = None
        if requst.user.group.exists():
            group = requst.user.groups.all()[0].name

        if group == 'customer':
            return redirect('dashboard')
        if group == 'admin':
            return view_func(requst, *args, **kwagrs)

    return wrapper_func