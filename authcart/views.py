from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
     if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            # messages.warning(request,"Password is Not Matching")
            return HttpResponse('password incorrect')
            return render(request,'signup.html')                   
        try:
            if User.objects.get(username=email):
                return HttpResponse("email already exist")
                # messages.info(request,"Email is Taken")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        # user.is_active=False
        user.save()
        return HttpResponse('user created',email)
        return render(request, 'signup.html')

def handlesignup(request):
    return render(request, 'login.html')


def handlesignup(request):
    return redirect('/auth/login')

def randpm():
    print("samir")