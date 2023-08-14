from django.contrib import admin
from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display = ('name','model','new','manafacture','location','price','discription','img','catagory','disable')