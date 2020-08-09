from django.contrib import admin
from book_tickets.models import *

# Register your models here.

admin.site.register(Passenger)
admin.site.register(Gender)
admin.site.register(Coach)
admin.site.register(Berth)
admin.site.register(TicketType)
