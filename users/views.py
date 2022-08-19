from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register a new user"""

    #if the request method is not post
    if request.method != 'POST':

        #display a blank registration form
        form = UserCreationForm()

    #if request is post
    else:

        #process the data
        #store the date entered by user 
        form = UserCreationForm(data=request.POST)

        #check if the form is valid 
        if form.is_valid():
            
            #make a new user 
            #and store the form's info to it
            new_user = form.save()

            #log the user
            login(request, new_user)

            #redirect the user to the home page
            return redirect('learning_logs:user_home')

    #display the form as per the above criterias are met
    context = {'form':form}
    return render(request,'registration/register.html', context)