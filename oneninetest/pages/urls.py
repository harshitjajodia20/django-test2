from django.urls import path
from . import views
urlpatterns = [
    path('login',views.login,name=('login') ),
    path('table',views.tables,name=('table') ),
    path('',views.login,name=('login')),
]
