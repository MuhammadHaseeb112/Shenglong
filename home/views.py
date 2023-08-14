from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import os
from django.views.decorators.cache import cache_control #new
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'aboutus.html')



def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            username = username.strip()
            password = password.strip()
            # user = auth.authenticate(username==username,password==password)
            user = auth.authenticate(username=username,password=password)
            

            if user is not None :
                print("you are login")
                messages.info(request, "Wellcome "+username)
                auth.login(request, user)
                request.session['username'] = username
                s_user= request.session['username']

                print('you are ' , request.session.get('username'))
                print('user = ', s_user)
                return redirect("home")
            else:
                messages.info(request, "invalid username or password")
                return redirect("login")

        else:
            return render(request,'login.html')
    else:
        messages.info(request, "your account is already login! please logout first")
        return redirect('home')
    

def logout(request):
    auth.logout(request)
    request.session.flush()
    request.session.clear_expired()
    print('you are ' , request.session.get('username'))
    return redirect('home')


def products(request):
    adds = product.objects.all().order_by('-id')
    paginator = Paginator(adds, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = 'a' * page_obj.paginator.num_pages
    return render(request, 'products.html',{'page_obj': page_obj,'nums': nums})

def products_catagory(request, catagory):
    print(catagory)
    adds = product.objects.filter(disable=False, catagory=catagory).order_by('-id')
    paginator = Paginator(adds, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    nums = 'a' * page_obj.paginator.num_pages
    return render(request, 'products.html',{'page_obj': page_obj,'nums': nums})



def registeration(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        firstname = firstname.strip()
        lastname = lastname.strip()
        email = email.strip()
        username = username.strip()
        password1 = password1.strip()
        password2 = password2.strip()

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('registeration')
            elif User.objects.filter(email=email).exists():
                print("Email already registered")
                messages.info(request, 'Email taken')
                return redirect('registeration')
            else:
                user = User.objects.create_user(email=email, password=password1, username=username, first_name=firstname, last_name=lastname)
                user.save();
                print('user created')
                messages.info(request, 'user created')
                return render(request, 'login.html')
    else:
        return render(request, 'register.html')



def view_product(request, id):
    add = product.objects.get(id=id)
    return render(request, 'view-product.html',{'add':add})


def admin_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            username = username.strip()
            password = password.strip()
            # user = auth.authenticate(username==username,password==password)
            user = auth.authenticate(username=username,password=password)

            


            if user is not None:
                if user.is_staff:
                    print("you are login")
                    messages.info(request, "Wellcome "+username)
                    auth.login(request, user)
                    request.session['username'] = username
                    s_user= request.session['username']

                    print('you are ' , request.session.get('username'))
                    print('user = ', s_user)
                    return redirect("manage_products")

                else:
                    messages.info(request, "You are not a staf member")
                    return redirect("admin_login")
            else:
                messages.info(request, "invalid username or password")
                return redirect("admin_login")

        else:
            return render(request,'admin_login.html')
    else:
        messages.info(request, "your account is already login! please logout first")
        return redirect('home')


def manage_products(request):
    if request.user.is_staff:
        adds = product.objects.all()
        paginator = Paginator(adds, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        nums = 'a' * page_obj.paginator.num_pages
        return render(request, 'manage_products.html', {'page_obj': page_obj,'nums': nums})
    else:
        return HttpResponse('you are not staff')


def manage_staff(request):
    if request.user.is_superuser:
        users = User.objects.filter(is_staff=True)
        paginator = Paginator(users, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        nums = 'a' * page_obj.paginator.num_pages
        return render(request,'manage_staff.html', {'page_obj': page_obj,'nums': nums})

    else:
        return HttpResponse('you are not admin')


def manage_user(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = User.objects.filter(is_staff=False)
            paginator = Paginator(users, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            nums = 'a' * page_obj.paginator.num_pages
            return render(request,'manage_user.html', {'page_obj': page_obj,'nums': nums})
        
        else:
            return HttpResponse('you are not admin')
    else:
        return redirect('login')


def add_staff(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                username = request.POST['username']
                email = request.POST['email']
                password1 = request.POST['password1']
                password2 = request.POST['password2']
                is_staff = request.POST['is_staff']
                
                print(is_staff)

                firstname = firstname.strip()
                lastname = lastname.strip()
                email = email.strip()
                username = username.strip()
                password1 = password1.strip()
                password2 = password2.strip()

                if password1==password2:
                    if User.objects.filter(username=username).exists():
                        messages.info(request, 'Username already taken')
                        return redirect('registeration')
                    elif User.objects.filter(email=email).exists():
                        print("Email already registered")
                        messages.info(request, 'Email taken')
                        return redirect('registeration')
                    else:
                        user = User.objects.create_user(email=email, password=password1, username=username, first_name=firstname, last_name=lastname, is_staff=is_staff )
                        user.save();
                        print('user created')
                        messages.info(request, 'user created')
                        return redirect('manage_staff')
            else:
                return render(request,'add_staff.html')
        else:
            return HttpResponse('you are not admin')
    else:
        messages.info(request, 'Please login First')
        return redirect('login')
    

def delete_user(request, id,username):
    if request.user.is_authenticated:
        print(id)
        print(username)
        user = User.objects.get(id=id,username=username)
        if user.is_staff==True and user.is_superuser==True:
            messages.info(request, "You can not delete Superuser")
            return redirect('manage_staff')
        elif user.is_staff==True and user.is_superuser==False:
            user.delete()
            messages.info(request, "Staff delete Successfully")
            return redirect('manage_staff')
        else:
            user.delete()
            messages.info(request, "User delete Successfully")
            return redirect('manage_user')
    else:
        messages.info(request, "Please login First")
        return redirect('login')


def add_product(request):
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        form.save()

        return redirect('manage_products')
    else:
        return render(request, 'add_product.html')


def delete_product(request, id):
    print(id)
    add = product.objects.get(id=id)
    add.delete()
    return redirect('manage_products')

def edit(request, id):
    if request.method == 'POST':
        add = product.objects.get(id=id)
        form = productForm(request.POST, request.FILES, instance=add)
        form.save()
        return redirect('manage_products')
    else:
        add = product.objects.get(id=id)
        return render(request, 'edit.html', {'add' : add})
    
def disable(request, id):
    add = product.objects.get(id=id)
    form = disable_productForm(request.POST, request.FILES, instance=add)
    form.save()
    return redirect('manage_products')




def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        print(message)
        print(email)
        print(name)

        send_mail(
            name,  #title
            message,   #message
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False,
        )
        messages.info(request, "we recived your mail ")
        return redirect('contact')
    else:
        return render(request, 'ContactUs.html')
    





def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('home')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form
        })
    else:
        messages.error(request, 'Please login first')
        return redirect('login')

        