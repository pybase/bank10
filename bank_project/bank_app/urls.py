from django.urls import path

from bank_app import views

app_name='bank_app'

urlpatterns=[
    path('',views.index,name='index'),
    path('details',views.details,name='details'),
    path('form',views.form,name='form')
]