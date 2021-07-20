from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='homepage'),
    path('UserRegisteration', views.reguser, name='Inv Register'),
    path('registeruserafter', views.registeruserafter, name="registerinvafter"),
    path('login', views.login, name='login'),
    path('loginafter', views.loginafter, name='loginafter'),
    path('Invest/', views.Investor, name="Investor"),
    path('Invest/update_investor/', views.update_investor, name="Investor Update"),
]
