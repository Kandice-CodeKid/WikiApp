from django.shortcuts import render, redirect
from .forms import UserForm, WikiForm, ExistingUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import WikiModel
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "wikiApp/index.html")


def landing(request):
    if request.method == "POST":
        # print(request.POST)
        newEntry = WikiModel(entryName=request.POST['entryName'], entryInfo=request.POST['entryInfo'],
                             foreignKey=request.user)
        newEntry.save()
        return redirect('landing')
    context = {
        'form': WikiForm,
        'myEntries': WikiModel.objects.filter(foreignKey=request.user)
    }
    return render(request, 'wikiApp/landing.html', context)


def edit(request):
    return render(request, 'wikiApp/edit.html')


def logIn(request):
    if request.method == 'POST':
        returnUser = authenticate(username=request.POST['username'], password=request.POST['password'])
        if returnUser is not None:
            login(request, returnUser)
            return redirect('landing')
        else:
            messages.error(request, 'Username or Password Incorrect, Please try again.')
            return redirect('logIn')
    context = {
        'form': UserForm
    }
    return render(request, "wikiApp/logIn.html", context)


def logOut(request):
    logout(request)
    return redirect('wikiApp/index.html')


def signUp(request):
    if request.method == 'POST':
        newUser = UserForm(request.POST)
        if newUser.is_valid():
            loggedInUser = User.objects.create_user(username=request.POST['username'], email='',
                                                    password=request.POST['password'])
            login(request, loggedInUser)
            return redirect('landing')
        else:
            context = {
                'form': UserForm(),
                'errors': UserForm.errors
            }
            return render(request, 'wikiApp/signUp.html', context)
    else:
        context = {
            'form': UserForm(),
            # 'errors': UserForm.errors
        }
        return render(request, 'wikiApp/signUp.html', context)
