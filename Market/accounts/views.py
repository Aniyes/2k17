from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Person, Profile
from product.models import Product



def home(request):

    return render(request, 'Home.html')

def login(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'Login.html', context)

    elif request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)
            # Redirect to a success page.
            context = {
                'user': user,
                'profile': Product.objects.get(user=user)

            }
            return render(request, 'Profile.html', context)

        else:
            # Return an 'invalid login' error message.
            form = AuthenticationForm(data=request.POST)
            context = {'form': form}
            return render(request, 'Login.html', context)


# Create your views here.
def create_person(request):

    if request.method == 'GET':
        form = UserCreationForm()

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        website = request.POST['website']
        gram_name = request.POST['gram_name']
        snap_name = request.POST['snap_name']
        email = request.POST['email']

        person = Person.objects.create_user(username=username, password=password,
                                            website=website, snap_name=snap_name,
                                            gram_name=gram_name)
        person.save()

        profile = Profile(user=person)
        profile.save()

        return redirect('/admin')
    context = {
        'form': form
    }

    return render(request, 'register.html', context)

def logout_view(request):

    logout(request)

    return redirect('/login')
