from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile, Songs
from django.conf import settings
from django.contrib.auth.decorators import login_required,permission_required
from .forms import RegisterForm, LoginForm,EditForm
import json
import urllib
import csv,io

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = RegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            

            if result['success']:
                if User.objects.filter(username=user_form.cleaned_data['username']).exists():
                    return render(request, 'users/register.html', {
                    'form': user_form,
                    'error_message': 'Username already exists.'
                })
                elif User.objects.filter(email=user_form.cleaned_data['email']).exists():
                    return render(request, 'users/register.html', {
                    'form': user_form,
                    'error_message': 'Email already exists.'
                })
                elif user_form.cleaned_data['password'] != user_form.cleaned_data['pass_confirm']:
                    return render(request, 'users/register.html', {
                        'form': user_form,
                        'error_message': 'Passwords do not match.'
                    })
                # elif not user_form.cleaned_data['profile_pic']:
                #     return render(request, 'users/register.html', {
                #         'form': user_form,
                #         'error_message': 'Upload Image!'
                #     })
                else:
                    # Create the user:
                    user = User.objects.create_user(
                    user_form.cleaned_data['username'],
                    user_form.cleaned_data['email'],
                    user_form.cleaned_data['password']
                    )

                    # profile_pic = request.FILES['']

                    UserProfile.objects.update_or_create(
                    user=user,
                    contact = user_form.cleaned_data['contact'],
                    fav_song = user_form.cleaned_data['fav_song'],
                    fav_artist = user_form.cleaned_data['fav_artist'],
                    profile_pic = user_form.cleaned_data['profile_pic'],
                    )

                    user.first_name = user_form.cleaned_data['first_name']
                    user.last_name = user_form.cleaned_data['last_name']
                    user.save()
                    
                    # UserProfile.save()
                    registered = True
            else:
                return render(request, 'users/register.html', {
                    'form': user_form,
                    'error_message': 'Invalid Captcha!!.'
                })
            
        else:
            print(user_form.errors)
    else:
        user_form = RegisterForm()
    return render(request,'users/register.html',{'form':user_form,'registered':registered})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('users:dashboard'))
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")
        
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})


@login_required
def profile(request):
     return render(request, 'users/profile.html',{})

@login_required
def edit_pic(request):
    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES)
        if form.is_valid():
            if not form.cleaned_data['profile_pic']:
               return render(request, 'users/edit_pic.html',{'form':form, 'error':'Something went wrong!! Please select your image.'})
            profile_pic = request.FILES.get('profile_pic') 
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.profile_pic = profile_pic
            user_profile.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = EditForm()
        return render(request, 'users/edit_pic.html',{'form':form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email= request.POST.get('email')
            user_profile = UserProfile.objects.get(user=user)
            user_profile.contact = request.POST.get('contact')
            user_profile.fav_song = request.POST.get('fav_song')
            user_profile.fav_song = request.POST.get('fav_artist')
            user.save()
            user_profile.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:

            print(form.errors)
            return render(request, 'users/edit_profile.html',{'form':form, 'error':'Something went wrong!!'})
    else:
        form = EditForm()
        return render(request, 'users/edit_profile.html',{'form':form})

@permission_required('admin.can_add_log_entry')
def song_upload(request):

    if request.method == 'GET':
        return render(request, 'song_upload.html',{})

    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('csv'):
         return render(request, 'song_upload.html', {'error':'Invalid file format!! Please upload .csv file only. '})

    dataset = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(dataset)
    next(io_string)
    for col in csv.reader(io_string,delimiter=',', quotechar='|'):
        _, created = Songs.objects.update_or_create(
            title = col[1],
            artist = col[0],
            duration = col[2]
        )

    return render(request, 'song_upload.html', {'message':'File uploaded successfully'})