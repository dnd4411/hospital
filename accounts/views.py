from django.contrib.auth import login, authenticate
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User


def home(request):
    return render(request, 'home.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            print(user)
               
            return redirect( 'login')
            
        else:
            error_mess = 'please enter valid username or password.'
            print(error_mess)
            return render(request, 'signup.html', {'error_message': error_mess,'form': form})
    else:
        form = SignUpForm()
        
        return render(request, 'signup.html', {'form': form})
    


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
    
        password = request.POST['password']
        print(username,'   ',password)
        user = authenticate( request, username=username, password=password)
        
        print(user)
        if user is not None:
            login(request, user)
            if (user.profile_type)=='D':
                print('docter')
                return render(request, 'docter_deshboard.html',{'user':user})
            else:
                print('pacient')
                return render(request, 'Patient_deshboard.html',{'user':user})
        else:
            
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')





def logout_view(request):
    logout(request)
    return redirect('home')