from django.contrib import admin
from .models import BookInfo

# Register your models here.

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    fields = ["book_file","title","author","description","language","category","upload_by"]


admin.site.site_header = "SaleLibrary admin"
admin.site.site_title = "SaleLibrary  admin"
admin.site.site_url = "http://saleLibrary.com/"
admin.site.index_title = "SaleLibrary administration"
admin.empty_value_display = "**Empty**"
