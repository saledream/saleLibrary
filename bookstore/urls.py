from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import path 
from . import views 

urlpatterns = [
    path("show",views.get_all_books,name="books"),
    path("book-detail/<slug:slug>/",views.book_detail,name="book-detail"),
    path("download/<slug:slug>/",views.book_download,name="download"),
    path("upload/",views.upload_books,name="upload"),
    path("edit-book/<int:id>",views.edit_book,name="edit-book"),
    path("search",views.search_index,name='search'),

]

