# contacts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add/', views.add_contact, name='add_contact'),  # Add contact page
    path('update/<int:contact_id>/', views.update_contact, name='update_contact'),  # Update contact page
    path('delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),  # Delete contact page
     path('search/', views.search_contact, name='search_contact'),  # Search contact page
]
