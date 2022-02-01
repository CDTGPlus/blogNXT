from .import views
from django.urls import path

urlpatterns = [
    #Note! by default, python treats views as functions, hence "as_view()" is not necessary in this application
    path('',views.translator_view,name='translator_view')
]