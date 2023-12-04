from django.http import HttpResponse
from django.shortcuts import redirect

def doutor(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "recepcionista":
            return redirect("recepcionista")

        if group == "doutor":
            return view_func(request, *args, **kwargs)

    return wrapper_function

def recepcionista(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == "doutor":
            return redirect("doutor")

        if group == "recepcionista":
            return view_func(request, *args, **kwargs)

    return wrapper_function
