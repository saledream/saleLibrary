from django.shortcuts import render
from bookstore.models import BookInfo
from django.contrib.auth.models import User 

# Create your views here.

def homepage(request):
    books = None 
    if request.user.is_authenticated:
        user = request.user 
        books = BookInfo.objects.filter(department=user.profile.department)[:10]
    else:
         books = BookInfo.objects.all()[:10]

    
    return render(request,"index.html",{"page":"home","books":books})


def aboutpage(request):
    
    user = User.objects.get(username="sale")

    return render(request,"about.html",{"page":"about","author":user}) 