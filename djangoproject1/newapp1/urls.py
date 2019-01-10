from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path('today/', views.today, name='today'),
    path('saurav/', views.saurav, name='saurav'),
    path('', views.index, name='index')
]



'''from django.conf.urls import patterns, include, url

urlpatterns = patterns('newapp1.views',
   url(r'^hello/', 'hello', name = 'hello'),
   url(r'^index/', 'index', name = 'index'),
   url(r'^hello/', 'hello', name = 'hello'),)

'''