from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save 
from django.core.validators import FileExtensionValidator
from bookstore.models import BookInfo 

# Create your models here.

PROFILE = "ProfilePhoto"
SEXS = (("male","Male"),
        ("female","Female")
        )


CHOICES = (
    ("",""),
    ("computer science","computer science"),
    ("marketing","marketing"),
    ("accounting and finance","accounting and finance")
)
def set_profile_photo(instance,filename):

    return os.path.join(PROFILE,"{}".format(instance,filename))

class UserProfile(models.Model):

        user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
        profile_photo = models.ImageField(upload_to="ProfilePhoto/%Y/%m/%d",blank=True,null=True)
        bio = models.CharField(max_length=50,blank=True,null=True)
        department  = models.CharField(max_length=255,choices=CHOICES)
        login_try = models.IntegerField(default=3)
class DownloadBook(models.Model):

    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="download_books",on_delete=models.CASCADE)
    download_date = models.DateTimeField(auto_now_add=True)

class UploadBooks(models.Model):
    book = models.ForeignKey(BookInfo,related_name="upload_books",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="upload_books",on_delete=models.CASCADE)
    download_date = models.DateTimeField(auto_now_add=True) 


        