from django.urls import path 
  
# importing views from views..py 
from . import views
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('pemilihan', views.pemilihan, name='pemilihan'),
    path('loginform', views.loginform, name='loginform'),
    path('konfirmasi', views.konfirmasi, name='konfirmasi'),
    path('donepage', views.donepage, name='donepage'),
    path('resetakuns', views.resetakuns, name='resetakuns'),
    path('resetted', views.resetted, name='resetted')
]