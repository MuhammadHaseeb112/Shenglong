from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('manage_products', views.manage_products, name='manage_products'),
    path('manage_staff', views.manage_staff, name='manage_staff'),
    path('manage_user', views.manage_user, name='manage_user'),
    path('products', views.products, name='products'),
    path('products_catagory/<str:catagory>', views.products_catagory, name='products_catagory'),
    path('registeration', views.registeration, name='registeration'),
    path('view_product/<int:id>', views.view_product, name='view_product'),
    path('manage_user', views.manage_user, name='manage_user'),
    path('add_staff', views.add_staff, name='add_staff'),  
    path('admin_login', views.admin_login, name='admin_login'),   
    path('delete_user/<int:id>&<str:username>', views.delete_user, name='delete_user'),  
    path('delete_product/<int:id>', views.delete_product, name='delete_product'), 
    path('edit/<int:id>', views.edit, name='edit'),   
    path('disable/<int:id>', views.disable, name='disable'),   
    path('add_product', views.add_product, name='add_product'),  

    # path('password_change', views.password_change, name='password_change'), 

    #new for change password
    # path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('change_password', views.change_password, name='change_password'),

    #for forgot password
    path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('accounts/', include('django.contrib.auth.urls')),
]
from django.conf.urls.static import static
from django.conf import settings
if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)