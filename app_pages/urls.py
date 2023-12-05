from django.urls import path
from . import views

urlpatterns = [
    #ex: /
    path('', views.home_page, name='home'),
    #ex: /contact/
    path('contact/', views.contact_page, name='contact'),
    #ex: /about/
    path('about/', views.about_page, name='about'),
    #ex: /account/
    path('account/', views.account_page, name='account')
]