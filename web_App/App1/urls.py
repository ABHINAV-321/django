from django.urls import path,include
from App1 import views

urlpatterns = [
    path('app1/',views.print_log),
    path('form/',views.form),
    path('edit/<pk>',views.edit),
    path('delete/<pk>',views.delete),
   # path('form/form1/',views.form_sub)
]
