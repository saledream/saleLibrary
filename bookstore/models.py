from django.db import models
from pdf2image import convert_from_path
from django.db.models.signals import post_save 
from django.conf import settings 
from django.contrib.auth.models import User 
from django.utils.text import slugify 
from django.shortcuts import reverse 
from django.utils import timezone
import os 
from  datetime  import datetime 
from django.core.validators import FileExtensionValidator
import math 

#from pyPDF2 import PdfFileReader 
from  pypdf import PdfReader 


# Create your models here.
CHOICES =(
            ("python","Python"),
            ("Kali linux","Kali linux"),
            ("Linux command","Linux command"),
            ("Networking","Networking"),
            ("Ethical hacking","Ethical hacking"),
            ("Django","Django"),
            ("Android","Android"),
            ("Kotlin","Kotlin"),
            ("Handout","Handout"),
            ("Javascript","javascript"),
        )

FILE_TYPE = (
            ("pdf","pdf"),
            ("docx","docx"),
            ("ppt","ppt")      
)
COVER_PAGE_DIRECTORY = "booksCover"
PDF_DIRECTORY = "booksPdf"
COVER_PAGE_FORMAT = "jpg"


def get_book_info(pdf_path):
     book_data = {}     
     reader = PdfReader(pdf_path)
     info = reader.metadata
     date = reader.metadata.creation_date.year
     size = ((os.path.getsize(pdf_path)/ 1024)/1024)

     book_data["size"]    = "%.1f MB" %(size) 
     book_data["published_year"]  = date
     book_data["pages"] = len(reader.pages)

    

     return book_data 


def set_pdf_filename(instance,filename):

    return os.path.join(PDF_DIRECTORY,"{}.pdf".format(instance,filename))

def set_cover_filename(instance,filename):
    return os.path.join(COVER_PAGE_DIRECTORY,"{}.{}".format(instance,filename,COVER_PAGE_FORMAT))


class BookInfo(models.Model):

     title = models.CharField(max_length=255,null=True,blank=True)
     author = models.CharField(max_length=255,null=True,blank=True)
     pages = models.IntegerField(null=True)
     size =  models.CharField(max_length=50,null=True)
     published_year =models.CharField(max_length=50,null=True)
     language = models.CharField(max_length=255,blank=True,null=True)
     upload_by = models.ForeignKey(User,related_name="uploaded_books",on_delete=models.CASCADE)
     description = models.TextField(null=True,blank=True)
     category = models.CharField(
       max_length = 255,choices=CHOICES,null=True,blank=True
        )
     upload_date = models.DateTimeField(auto_now_add=True)
     cover  = models.ImageField(upload_to=set_cover_filename,null=True,blank=True)
     book_file = models.FileField(upload_to=set_pdf_filename, max_length=255,null=True,
    validators = [FileExtensionValidator(allowed_extensions=["pdf","ppt","docx"])])
     file_type = models.CharField(max_length=255,choices=FILE_TYPE,default="pdf")
     slug = models.SlugField(unique_for_date=upload_date,blank=True,null=True)
     department = models.CharField(max_length=255,null=True,blank=True)
     def book_url(self):

        return reverse("bookstore:book-detail",args="%s"%str(self.slug))

     def save(self,*args,**kwargs):
        if self.title == '':
            self.title = "Not provided" + str(timezone.now())

        self.slug = slugify(self.title) 
        super().save(*args,**kwargs)   


class Book_info(models.Model):
    book_name = models.CharField(max_length=150, null=False)
    author = models.CharField(max_length=50, null=False)
    category = models.CharField(max_length=700, null=True)
    price = models.IntegerField(null=True)
    edition = models.CharField(max_length=150, null=True)
    publisher = models.CharField(max_length=150, null=True)
   
def convert_pdfto_image(sender,instance,created,**kwargs):

    if created:
        cover_page_dir = os.path.join(settings.MEDIA_ROOT,COVER_PAGE_DIRECTORY)
        if not os.path.exists(cover_page_dir):
            os.mkdir(cover_page_dir)

        cover_page_image = convert_from_path(
                instance.book_file.path,
                dpi=200,
                first_page = 1,
                last_page = 1,
                fmt = COVER_PAGE_FORMAT,
                output_folder = cover_page_dir,
        )[0]

        pdf_filename,extension = os.path.splitext(os.path.basename(instance.book_file.name))

        new_cover_page_path = '{}.{}'.format(os.path.join(cover_page_dir,pdf_filename),COVER_PAGE_FORMAT)

        os.rename(cover_page_image.filename,new_cover_page_path)
        new_cover_page_path_relative = '{}.{}'.format(os.path.join(COVER_PAGE_DIRECTORY,pdf_filename),COVER_PAGE_FORMAT)
        
        book_data = get_book_info(instance.book_file.path)
        instance.cover = new_cover_page_path_relative
        instance.published_year = book_data["published_year"]
        instance.pages = book_data["pages"]
        instance.size = book_data["size"]
        instance.save()


post_save.connect(convert_pdfto_image,sender=BookInfo)
