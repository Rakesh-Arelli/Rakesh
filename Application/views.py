from django.shortcuts import render,HttpResponseRedirect
from .forms import PatientForm
from .models import PatientModel
from django.contrib import messages
from .forms import signUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home1(request):
    return render(request,'home.html')
# def contact1(request):
#     return render(request,'contact.html')
def about1(request):
    return render(request,'about.html')

def show(request):

    if request.method == 'POST':
        ob = PatientForm(request.POST)
        if ob.is_valid():
            print("Form Validated")
            nm=ob.cleaned_data['name']
            ag=ob.cleaned_data['age']
            gen=ob.cleaned_data['Gender']
            sta=ob.cleaned_data['startCity']
            des=ob.cleaned_data['Destination']
            pri=ob.cleaned_data['price']

            all_details=PatientModel(name=nm,age=ag,Gender=gen,startCity=sta,Destination=des,price=pri)
            all_details.save()
            ob = PatientForm()
            messages.add_message(request,messages.SUCCESS,'Details submited successfully')
        return HttpResponseRedirect('/contact')



    else:
        ob = PatientForm()
    det=PatientModel.objects.all()
    return render(request,'contact.html',{'form':ob,'details':det})

#this is for update

def update(request,id):
    if request.method =='POST':
        pi=PatientModel.objects.get(pk=id)
        fm=PatientForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.ERROR, f'  ID no {id} Details updated successfully!!!')
            messages.error(request,'now you see the details')
        return HttpResponseRedirect('/contact')

    else:
        pi=PatientModel.objects.get(pk=id)
        fm=PatientForm(instance=pi)
    return  render(request,'updatedetails.html',{'form':fm})

#
# # This Function will Delete
def delete_data(request,id):
    if request.method == 'POST':
        pi = PatientModel.objects.get(pk=id)
        pi.delete()
        messages.add_message(request, messages.INFO, f'  ID no {id}  Information deleted successfully')
        return HttpResponseRedirect('/contact')

#sign_up view function
def sign_up(request):
    if request.method=='POST':
        fm=signUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            fm.save()
    else:
        fm=signUpForm()
    return render(request,'signin.html',{'form':fm})

#log in view form

def log_in(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            unm=fm.cleaned_data['username']
            pwd=fm.cleaned_data['password']
            data=authenticate(username=unm,password=pwd)
            if data is not None:
                login(request,data)
                messages.success(request,'login successfull!!!!')
                return HttpResponseRedirect('/profile')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})

def user_profile(request):
    return render(request,'profile.html')

#log out form

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login')




