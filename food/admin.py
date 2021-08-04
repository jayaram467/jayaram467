
from django.contrib import admin
from .models import ordernow,contactus
class Adminordernow(admin.ModelAdmin):
    list_display=[]
class Admincontactus(admin.ModelAdmin):
    list_display=[]


    


admin.site.register(ordernow,Adminordernow)
admin.site.register(contactus,Admincontactus)

