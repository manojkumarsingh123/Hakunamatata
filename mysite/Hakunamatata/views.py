from django.shortcuts import render
from Hakunamatata.forms import contactform_,UserForm,UserProfileInfoForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
#if you want something after logged in of user then use decorators login_required



# Create your views here.

def base(request):
    return render(request,'Hakunamatata/base.html')

def home(request):
    return render(request,'Hakunamatata/base.html')



def about(request):
    return render(request,'Hakunamatata/about.html')
#def index(request):
#    return render(request,'Hakunamatata/index.html')


@login_required
def special(request):#here we can manage that what we want to show user when they logged in
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/Hakunamatata/user_login/'
    return render(request,'Hakunamatata/special.html')

@login_required # these are decorators
def user_logout(request):#we want here only login user can logged out
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('base'))




















def contactform(request):
    form = contactform_()


    if request.method == 'POST':#when hit submit then
        form =contactform_(request.POST)#we pass request.post

        if form.is_valid():#you can use here own custom validator
            form.save(commit=True)#mns valid then details save in database

            return base(request)#and after save redirect to homepage
        else:
            print("ERROR!")

    return render(request,'Hakunamatata/contact.html',{'form':form})
#otherwise return to the again contact form



def register(request):

    registered = False #tells us someone registeredor not

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user # this line indicate one to one releationship that we used in models
                 #profile.user = user(which is equal to user form) which goes to form folder user form and model = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']
#request.FILES using while uploading any type of file like pdf,jpg,cv

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'Hakunamatata/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

#last in inside {we are passing here context dictionary with key:value pair}
# rememeber that key must same as you used in registration.html homepage
#these are the key
 #user_form'
 # 'profile_form'
 # 'registered'




def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        #using .get('username') to grab user name from login.html username
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('special'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'Hakunamatata/login.html', {})











#from django.shortcuts import render,redirect
#from django.http import HttpResponse# import HttpResponse
#from .forms import ContactForm
# Create your views here.
#def base(request):#in place of request we can take any name
#        return render (request,'base.html')
# Create your views here.










































#def contact(request):#in place of request we can take any name
#   contact_form = ContactForm(request.POST or None)
#   context = {
#        "title":"Contact",
#        "content":" Welcome to the contact page.",
#        "form": contact_form,
#    }
#  if request.method == "POST": # below down method is work when you fill your form and same time you can able to see filling data in cmd
#        print(request.POST.get('fullname'))
#        print(request.POST.get('email'))
#        print(request.POST.get('content'))
 #  return render (request,"Hakunamatata/contact.html",context)
