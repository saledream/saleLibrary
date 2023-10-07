from django.shortcuts import render,redirect,reverse,get_object_or_404 
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages 
from django.contrib.auth.models import User 
from .forms import SignUpForm,ProfileForm ,LoginForm, SetPassWordForm,UserEditForm,ProfileEditForm  
from .models import UserProfile,DownloadBook,UploadBooks 

# Create your views here.

def user_login(request):
    number_of_tries = 3
    login_error_msg = ''
    if request.method == "POST":
        login_form = LoginForm(request.POST)
   
        if login_form.is_valid():
            form_data = login_form.cleaned_data 

            user = authenticate(username=form_data['username'],password=form_data['password'])
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    
                    return redirect(request.GET.get('next',"/"))

                else:
                    login_error_msg = "Your Account is blocked!"

            else:
                login_error_msg = "Wrong username or password!"
               
        else:
            login_error_msg = "Invalid login"
    else:
        login_form = LoginForm()            
    return render(request,"login.html",{"form":login_form,"error_msg":login_error_msg,"page":"signin"})

def user_logout(request):
    logout(request)
    return redirect("/books/show")

def user_signup(request):
    account_created = False 
    new_user = None 
    signup = SignUpForm()
    if request.method == "POST":

        singup_form = SignUpForm(request.POST)

        if singup_form.is_valid():
            new_user = singup_form.save(commit=False) 
            new_user.set_password(singup_form.cleaned_data["password"])
            new_user.save()
            profile = UserProfile(user=new_user)
            profile.save()
            messages.success(request,"You successfully create account")
            account_created = True
            
    return render(request,"signup.html",{"form":signup,"page":"signin","create_successfully":account_created,"new_user":new_user})
@login_required 
def password_change(request):
    
    user = request.user 
    form = SetPassWordForm(user) 

    return render(request,"registration/password_reset_confirm.html",{"form":form})  
    
def showMyProfile(request):
    download_books = None 
    upload_books = None
    username = request.GET.get("q",None)

    user = User.objects.get(username=username)
    
    download_books = DownloadBook.objects.filter(user=user)
    upload_books = UploadBooks.objects.filter(user=user)

    user_form = UserEditForm(instance=user)
    profile = ProfileForm(instance=user.profile)

    return render(request,"showprofile.html",
    {
    "userform":user_form,
    "profile":profile,
    "user":user,
    "d_book":download_books,
    "u_book":upload_books}
    ) 


@login_required 
def editMyProfile(request):

    user = request.user 
    if request.method == "POST":
        user_form = UserEditForm(request.POST,instance=user) 
        profile = ProfileEditForm(request.POST,request.FILES,instance=user.profile)

        if user_form.is_valid and profile.is_valid():
            user_form.save()
            profile.save()
            return redirect(reverse("account:show_profile",args=(user.username,)))
        else:
            print("Error")

    else:
        profile = ProfileEditForm(instance=user.profile)
        userform = UserEditForm(instance=user)

    return render(request,"editmyprofile.html",{"userform":userform,"profile":profile}) 
