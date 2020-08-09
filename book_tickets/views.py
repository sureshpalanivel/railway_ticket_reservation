from django.shortcuts import render,  redirect, get_object_or_404, get_list_or_404

# Create your views here.
from .forms import *

from django.http import HttpResponse

def index(request):
    return HttpResponse('Book your tickets..')

def bookticket (request):   
    form = TicketForm()   
    context = {'form': form} 
    return render (request, 'book_tickets/booking_form.html', context)
    #return render (request, 'tickets/main.html', context)

def ticketStatus (request, pk):   
    context = {'pk': pk} 
    return render (request, 'book_tickets/ticket_status.html', context)