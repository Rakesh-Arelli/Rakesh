from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.home1,name='home'),
    path('contact/',views.show,name='contact'),
    path('about/',views.about1,name='about'),
    path('sign/',views.sign_up,name='signin'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('profile/',views.user_profile,name='profile'),
    path('delete/<int:id>/',views.delete_data,name='deletedata'),
    path('update/<int:id>/',views.update,name='updatedata')

]