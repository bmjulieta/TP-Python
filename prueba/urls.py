from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views


urlpatterns = [
    path('',views.inicio,name="index"),
    path('login/',views.login,name="login"),
    path('create/',views.create,name="create"),
    path('edit/<id>/',views.edit,name="edit"),
    path('delete/<id>/',views.delete,name="delete"),
    path('contactanos/',views.contactanos,name="contactanos"),
    path('blog/',views.blog ,name="blog"),
    path('about_us/',views.about_us ,name="about_us"),
    path('nt/',views.nt ,name="NuestrosTalentos"),
    path('servicios/',views.servicios ,name="servicios"),
    path('shop/',views.shop ,name="shop"),
    path('regi/',views.regi,name="regi"),
   
]
