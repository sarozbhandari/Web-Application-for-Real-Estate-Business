from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact


def register(request):
    #GET FORM VALUES
    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #CHECKING VALIDATION
        if password == password2:
            #Check Username
            if User.objects.filter(username = username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                    #Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'Login Successful')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are registered and now can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')





def login(request):
    if request.method == "POST":
       #Login
       username = request.POST['username']
       password = request.POST['password']
       
       user = auth.authenticate(username = username, password = password)
       if user is not None:
           auth.login(request, user)
           messages.success(request, 'Login Successful')
           return redirect('dashboard')
       else:
           messages.error(request, 'Inavlid Credentials')
           return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "Logged out successfully")
        return redirect('index')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
