from app1 import views
from django.urls import path




urlpatterns=[
    path('',views.base,name='home'),
    path('sign/',views.signup1,name='signup'),
    path('login1/',views.login1,name='login'),

]