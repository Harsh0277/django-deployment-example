from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from first_app.models import Topic,Webpage,AccessRecord
from first_app import forms
from first_app.forms import FormName,UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #return HttpResponse('<em>Hello World!</em>')
    #my_dict={'insert_me':'Hello! I am from views.py'}
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    return render(request,'first_app/index.html',context=date_dict)

def home(request):
    return HttpResponse('<em>Hello World!</em>')

def form_name_view(request):
    form=FormName()

    if request.method=="POST":
        form=forms.FormName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("Error Form Invalid")

    return render(request,'first_app/form_page.html',{'form':form})

def other(request):
    context_dict={'text':'hello world','number':100}
    return render(request,'first_app/other.html',context_dict)

def relative(request):
    return render(request,'first_app/relative_url_templates.html')

def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'first_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'first_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def special(request):
    return HttpResponse("You are logged in, Great!")

# def form_name_view(request):
#     form=forms.FormName()
#
#     if request.method=="POST":
#         form=forms.FormName(request.POST)
#         if form.is_valid():
#             print("Validation Success")
#             print("Name: "+form.cleaned_data['name'])
#             print("Email: " + form.cleaned_data['email'])
#             print("Text: " + form.cleaned_data['text'])
#
#     return render(request,'first_app/form_page.html',{'form':form})