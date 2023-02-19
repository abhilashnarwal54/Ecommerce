from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm
urlpatterns = [
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact',views.contact, name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name="category"),
    path('category-title/<val>',views.CategoryTitle.as_view(),name="category-title"),
    path('product-detail/<int:pk>',views.ProductDetail.as_view(),name="product-detail"),
    path('profile',views.ProfileView.as_view(), name='profile'),
    path('address',views.address, name='address'),
    path('updateaddress/<int:pk>',views.UpdateAdress.as_view(), name='updateaddress'), 

    #login authatication 
    path('reg',views.Registration, name="register"),
    path('login',views.Login, name='login'),
    path('logout',views.Logout, name='logout'),
    #reseting the password for the login page using the ingbuilt django MyPasswordResetForm we don't need to write any views function manually we directly write these url
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm),name='password_reset'),
    #for change password for the change password page we are using the  inbuilt django PasswordChangeForm for changing the password and add new passowrd
    #we are creating the two pats for the change password ond for the changepassword and another is after chage password we redirect to the another url it will shows the sucess message
    path('changepassword/',auth_view.PasswordChangeView.as_view(template_name='passwordchange.html',form_class = MyPasswordChangeForm,success_url = '/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)