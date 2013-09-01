# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from user.forms import RegistrationForm
def sign_user(request):
    dict={}
    form2=RegistrationForm()
    if request.POST:
        form2=RegistrationForm(request.POST)
        if form2.is_valid:
            print "Form Valid"
            form2.save()
            response=redirect('/')
            return response
        else:
            print"Invalid Form"
    dict['form2']=form2
    return render_to_response('signup.html',dict,context_instance=RequestContext(request))


def login_user(request):
    state = "Please login below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
            
    return render_to_response('auth.html',{'state':state, 'username': username},RequestContext(request))

#def login_user(request):
#    state = "Please login below..."
#    if request.POST:
#        email = request.POST.get('email')
#        password = request.POST.get('password')
#        
#        user = authenticate(email=email, password=password)
#        if user is not None:
#            if user.is_active:
#                login(request, user)
#                state = "You're successfully logged in!"
#            else:
#                state = "Your account is not active, please contact the site admin."
#        else:
#            state = "Your username and/or password were incorrect."
#            
#    return render_to_response('auth.html',{'state':state})