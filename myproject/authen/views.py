from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.


def login_(request):

    login_nav=True
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        u=authenticate(username=username,password=password)
        if u is not None:
            login(request,u)
            return redirect('home')
        else:
            messages.add_message(request,messages.ERROR,'login Failed !!! put correct credentials')
            return redirect('login_')
    return render(request,'login_.html',{'login_nav':login_nav})


def Register(request):
    login_nav=True
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
            # messages.add_message(request,messages.INFO,'username already taken please use diffent username !!!')
            messages.add_message(request,messages.WARNING,'username already taken please use diffent username !!!')

        except:
            u=User.objects.create(first_name=firstname,
                                last_name=lastname,
                                email=email,
                                username=username,)
            u.set_password(password)
            u.save()
            return redirect('login_')

    return render(request,'Register.html',{'login_nav':login_nav})


def logout_(request):

    logout(request)

    return redirect('login_')


def profile(request):

    return render(request,'profile.html')

def changepass(request):

    if request.method == 'POST':
        newpass=request.POST['password']
        print(newpass)

        u=User.objects.get(username=request.user)
        u.set_password(newpass)
        u.save()
        return redirect('logout_')


    return render(request,'changepassword.html')