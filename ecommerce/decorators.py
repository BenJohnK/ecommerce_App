from django.shortcuts import redirect

def is_authenticated(func_view):
    def wrapper(request,*args,**kwargs):
        if(request.user.is_authenticated):
            return redirect('/')
        else:
            return func_view(request,*args,**kwargs)
    return wrapper
    
