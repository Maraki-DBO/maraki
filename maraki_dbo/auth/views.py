from django.shortcuts import render


'''
 View for the AUTHENTICATION part to be able to login by using their emails, phone number, or username

# Create your views here.
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
        else:
            # Invalid credentials, show an error message
            pass
    else:
        # Render the login form
        pass
'''