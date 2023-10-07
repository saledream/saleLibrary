from django.shortcuts import render, get_object_or_404,redirect,reverse
from .models import BookInfo 
from django.http import HttpResponse,JsonResponse 
from django.core.paginator import  Paginator, PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required 
import mimetypes 
import os 

from account.models import DownloadBook, UploadBooks 
from account.forms import EditBookForm,UploadFileForm  
# Create your views here.

def get_all_books(request):
    # add pagination 
    books = None 
    book_category = "Random Books List"
    categorys = ["All"]
    load_all_category = BookInfo.objects.all()

    for record in load_all_category:
        if record.category not in categorys:
            categorys.append(record.category)


    books_category = request.GET.get("q")
    
    if books_category is None and request.user.is_authenticated:
        books = BookInfo.objects.filter(department__icontains=request.user.profile.department)
        book_category = "Recommended Books List"
    elif books_category:
            if books_category == "all":
                        books = BookInfo.objects.all()
                        book_category = " All Books List"
            else:             
                books = BookInfo.objects.filter(category=books_category)
                book_category = "%s Books List" %(books_category)
    else :
         books = BookInfo.objects.all()
    pages = Paginator(books,2) 
    page = request.GET.get("page")    # extraction of request data

    try:
        boks= pages.page(page)
        page = int(books) 
    except PageNotAnInteger:
        boks = pages.page(1)
        
    except EmptyPage:
        boks = pages.page(pages.num_pages) 

   

    return render(request,"books.html",
        {"books":books,
        "page":"books",
        "bc":book_category,
        "category":categorys})

def book_detail(request,slug):
    categorys = ["All"]
    load_all_category = BookInfo.objects.all()
    for record in load_all_category:
        if record.category not in categorys:
            categorys.append(record.category)

    book = get_object_or_404(BookInfo,slug=slug)
    
    return render(request,"book-detail.html",{"book":book,"page":"books","category":categorys})   

@login_required(login_url="/accounts/login/")
def book_download(request,slug):
   
    book_file_obj = get_object_or_404(BookInfo,slug=slug)
    book_file_path = book_file_obj.book_file.path 
    filename = book_file_obj.book_file.name 

    file_obj = open(book_file_path,'rb')

    mime_type, _ = mimetypes.guess_type(book_file_path)
    response = HttpResponse(file_obj,content_type=mimetypes)
    response['Content-Disposition'] = "attachment;filename=%s" %filename  
    download_book = DownloadBook(book=book_file_obj,user=request.user)
    download_book.save()
    
    return response  

@login_required(login_url="/accounts/login/") 
def upload_books(request):
    book_exist = None 
    if request.method == "POST":
        upload_form = UploadFileForm(request.POST,request.FILES) 
        print("posting .....")
        if upload_form.is_valid():
            
            new_book = upload_form.save(commit=False)
            new_book.upload_by = request.user 
            new_book.save()
            upload = UploadBooks(book=new_book,user=request.user)
            upload.save()
            return redirect(reverse("bookstore:edit-book",args=(new_book.id,))) 
            
        else:
            print(upload_form.errors)
    upload_form = UploadFileForm()
    print("wwwwwww")
    return render(request,"upload_book.html",
        {"upload_form":upload_form,
        "page":"upload",
        'b_exist': book_exist
        }) 
@login_required(login_url="/accounts/login/")
def edit_book(request,id):
     
     book = get_object_or_404(BookInfo,id=id)

     if request.method == 'POST':
         edit_form =  EditBookForm(request.POST,request.FILES,instance=book)
         if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse("bookstore:book-detail",args=(book.slug,)))
        
         
     edit_form = EditBookForm(instance=book)
     return render(request,"edit-book.html",
        {"form":edit_form,
        "page":"books",
        "book":book})

def search_index(request):
    
    query = request.GET.get("q")
    book_data = []
    if query:

        books_by_title = BookInfo.objects.filter(title__icontains=query)
        books_by_category = BookInfo.objects.filter(category__icontains=query)
        books_by_department = BookInfo.objects.filter(department__icontains=query)
       
        for books in (books_by_title,books_by_department,books_by_category):
             
             for book in books:
                single_book = {}
                single_book["cover"] = book.cover.url
                single_book['slug']  = book.slug
                single_book["size"]  = book.size 
                single_book["language"] = book.language 
                single_book["page"] = book.pages 
                single_book["file_type"] = book.file_type 
                single_book["title"] = book.title 
                
                book_data.append(single_book)

            
        return JsonResponse(book_data,safe=False,status=200)
    else:
        pass 

    return JsonResponse("No query",status=400)