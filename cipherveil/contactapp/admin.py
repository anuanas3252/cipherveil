from django.contrib import admin

# Register your models here.
from .models import ContactBook, OpenID

class ContactBookAdmin(admin.ModelAdmin):
    list_display = ('id','name','tag')
    #search_fields = ('id','name','tag')

    
    

class OpenIDAdmin(admin.ModelAdmin):
    list_display = ('id','tag')
    #search_fields = ('id','tag')



admin.site.register(OpenID,OpenIDAdmin)
admin.site.register(ContactBook,ContactBookAdmin)