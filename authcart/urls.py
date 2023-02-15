from django.urls import path
from authcart import views


urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.handlesignup, name='handlelogin'),
    path('logout/',views.handlesignup, name='handlelogout'),
]
