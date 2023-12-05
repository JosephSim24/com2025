from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #ex: /
    path('', views.home_page, name='home'),
    #ex: /contact/
    path('contact/', views.contact_page, name='contact'),
    #ex: /about/
    path('about/', views.about_page, name='about'),
    #ex: /account/
    path('account/', views.account_page, name='account'),
    #ex: /recommend-a-friend?album=:id/
    path('recommend-a-friend', views.recommend_page, name='recommend'),
    #ex: /account/login/
    path('account/login/', LoginView.as_view(template_name='app_pages/login.html'), name='login'),
    #ex: /account/logout/
    path('account/logout/', LogoutView.as_view(next_page='/'), name='logout'),
]