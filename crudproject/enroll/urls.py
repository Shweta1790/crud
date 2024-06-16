from django.urls import path
from . import views
urlpatterns = [
    path('', views.insert_print, name= 'insertprint'),
    path('delete/<int:id>/', views.delete_record, name='delete_record'),
    path('edit/<int:id>', views.edit, name= 'edit'),
]
