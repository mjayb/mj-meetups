from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
#from django.contrib.auth.forms import UserCreationForm
from .models import Meetup, Participant
from .forms import RegistrationForm,  MyUserRegistrationForm, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse

# Create your views here.
def loginPage(request):
    page='Login'
    if request.user.is_authenticated:
        return redirect('meetups')
    #when submit botti=on is pressed 
    if request.method=='POST':  
        email = request.POST.get('email')
        email.lower()
        password = request.POST.get('password')
        try:
            user=myUser.objects.get(email=email)  
        except:
            messages.error(request, 'User does not exist')
        user=authenticate(request, email=email, password=password)
        if user is not None:
          login(request, user)
          return redirect ('meetups')
        else:
          messages.error(request, 'Username OR password does not exit')
    context={'page':page}

    return render(request, 'meetups/login.html', context)

def register(request):
    page='Register'
    form=MyUserRegistrationForm()
    context={'form':form,  'page':page}

    if request.method == 'POST':
        form = MyUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            #email=user.email
            user.save()
            #send_mail('Thanks for registering','Thanks For Registering, we will get i touch with you soon..', settings.EMAIL_HOST_USER, [ email,])
            login(request, user)
            return redirect('meetups')
        else:
            messages.error(request, 'An error occurred during registration')
           
    return render(request, 'meetups/register.html',context )

@login_required(login_url='login')
def profile(request, pk):
    message=False
    success=messages.success(request, 'Your profile is updated successfully')
    page="Profile"
    user = request.user
    form = Profile(instance=user)

    if request.method == 'POST':
        form = Profile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            success=messages.success(request, 'Your profile is updated successfully')
            message=True
            return redirect('profile', pk=user.id )
            #return redirect('update_success',  )
    context={'form':form, 'page':page, 'message':message, 'success':success}
    return render(request, 'meetups/profile.html', context)    




def index(request):
    meetups=Meetup.objects.all() 
    search=request.GET.get('q') if request.GET.get('q')!=None else ''
    meetups=meetups.filter(
        
        Q(title__icontains=search)|
        Q(description__icontains=search)
    
        )
    return render(request, 'meetups/meetup.html', {'meetups':meetups} )



def meetup_details(request, meetup_slug):
   # selected_meetup=Meetup.objects.get(slug=meetup_slug)
    try:
        selected_meetup=Meetup.objects.get(slug=meetup_slug)
        if request.method=='GET':
            registration_form=RegistrationForm()
        else:
            registration_form= RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant=registration_form.save()
                selected_meetup.participant.add(participant)
                #return redirect('confirm-registration')
                return redirect('confirm_registration')
                
        return render(request, 'meetups/meetup_details.html', {
         'meet_found':True,
         'meetup':selected_meetup,
         'form': registration_form 
          })    
   
    except Exception as exc:
        return render(request, 'meetups/meetup_details.html', {
         'meet_found':False,
         'meetup':selected_meetup
         
     })


def confirm_registration(request):
   return render(request, 'meetups/registration_success.html')

def meetup_about(request):
    return render(request, 'meetups/meetup_about.html' ) 

def meetup_services(request):
    return render(request, 'meetups/meetup_services.html' ) 

def meetup_team(request):
    return render(request, 'meetups/meetup_team.html') 

def meetup_contact(request):
    return render(request, 'meetups/meetup_contact.html') 

def reg_error(request):
    return render(request, 'meetups/reg_error.html')    

def update_success(request):
    return render(request, 'meetups/update_success.html') 


def logoutUser(request):
    logout(request)
    return redirect('meetups')