
from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('book/', views.bookticket, name='book'),  
    path('status/<int:pk>/', views.ticketStatus, name='ticket_status'),  
]
