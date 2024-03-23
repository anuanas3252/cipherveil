from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'frontlineapp/index.html', {'page': 'index'})



def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        return render(request, 'frontlineapp/home.html', {'page': 'home'})
    else:
        # Redirect to the signin page if the user is not authenticated
        return redirect('signin')



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'frontlineapp/signin.html', {'page': 'signin'})



def signout(request):
    # Clear the session and log the user out
    logout(request)
    return redirect('signin')