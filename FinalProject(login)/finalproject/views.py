from django.shortcuts import redirect

def login_redirect(request):
    return redirect('/map/login')

def register_redirect(request):
    return redirect('/map/login')