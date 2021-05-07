from django.shortcuts import redirect

def is_authenticated(func_view):
    def wrapper(request,*args,**kwargs):
        if(request.user.is_authenticated):
            return redirect('/')
        else:
            return func_view(request,*args,**kwargs)
    return wrapper
    
def is_admin(func_view):
    def wrapper(request,*args,**kwargs):
        if request.user.is_superuser:
            return redirect('/admin/home/')
        return func_view(request,*args,**kwargs)
    return wrapper

def admin_only(func_view):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect('/')
        return func_view(request,*args,**kwargs)
    return wrapper