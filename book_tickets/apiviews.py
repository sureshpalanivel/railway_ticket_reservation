from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from book_tickets.models import *
from book_tickets.serializers import *
from django.urls import reverse_lazy

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Q
from datetime import datetime

# Create your views here.

#PURE DJANGO VIEWS
# def pasenger_list(request):
#     # MAX_OBJECTS = 5
#     # polls = Poll.objects.all()[:MAX_OBJECTS]
#     data = {'results': PassengerDetails.objects.all()}
#     return JsonResponse(data)

#@method_decorator(csrf_exempt, name='dispatch')
class FormData(APIView):
    passengers = Passenger.objects.all().filter(child=False)
    total_tickets = passengers.count()
    def get(self, request): 
        gender = Gender.objects.all()
        berth = Berth.objects.all()
        gender_data = GenderSerializer(gender, many=True).data
        berth_data = BerthSerializer(berth, many=True).data
        return Response({'gender':gender_data,'berth':berth_data})       
        #return Response({'gender':gender_data,'berth':berth_data, 'count':a.tickets_count})       

class BookTickets(APIView):

    passengers = Passenger.objects.all().filter(child=False)
    tickets_cnt = passengers.count()
    s1_cnt = passengers.filter(Q(coach='S1')).count()
    s1_upper = passengers.filter(Q(coach='S1'),Q(berth_preference='UPR')).count()
    s1_lower = passengers.filter(Q(coach='S1'),Q(berth_preference='LWR')).count()
    s1_mid = passengers.filter(Q(coach='S1'),Q(berth_preference='MID')).count()
    s1_sid = passengers.filter(Q(coach='S1'),Q(berth_preference='SID')).count()

    s2_cnt = passengers.filter(Q(coach='S2')).count()
    s2_upper = passengers.filter(Q(coach='S2'),Q(berth_preference='UPR')).count()
    s2_lower = passengers.filter(Q(coach='S2'),Q(berth_preference='LWR')).count()
    s2_mid = passengers.filter(Q(coach='S2'),Q(berth_preference='MID')).count()
    s2_sid = passengers.filter(Q(coach='S2'),Q(berth_preference='SID')).count()

    s3_cnt = passengers.filter(Q(coach='S3')).count()
    s3_upper = passengers.filter(Q(coach='S3'),Q(berth_preference='UPR')).count()
    s3_lower = passengers.filter(Q(coach='S3'),Q(berth_preference='LWR')).count()
    s3_mid = passengers.filter(Q(coach='S3'),Q(berth_preference='MID')).count()
    s3_sid = passengers.filter(Q(coach='S3'),Q(berth_preference='SID')).count()

    s4_cnt = passengers.filter(Q(coach='S4')).count()
    s4_upper = passengers.filter(Q(coach='S4'),Q(berth_preference='UPR')).count()
    s4_lower = passengers.filter(Q(coach='S4'),Q(berth_preference='LWR')).count()
    s4_mid = passengers.filter(Q(coach='S4'),Q(berth_preference='MID')).count()
    s4_sid = passengers.filter(Q(coach='S4'),Q(berth_preference='SID')).count()

    def post(self, request):  
        data = {}
        name = request.data.get('name')
        age = request.data.get('age')
        gender = request.data.get('gender')
        
        if self.tickets_cnt < 37:
            if int(age) > 5:  
                if self.tickets_cnt <= 24:
                    ticket_type = 'CF'
                elif self.tickets_cnt > 24 and self.tickets_cnt <= 32:
                    ticket_type = 'RAC'
                elif self.tickets_cnt > 32 and self.tickets_cnt <= 37:
                    ticket_type = 'WL'
                else:
                    return Response({'error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST) 

                if int(age) > 60:                  
                    lower = self.check_lower()
                    if len(lower) != 0:
                        coach = lower 
                        berth_preference = 'LWR'
                    else:
                        mid = self.check_mid()
                        if len(mid) != 0:
                            coach = mid 
                            berth_preference = 'MID'
                        else:                    
                            upper = self.check_upper()
                            if len(upper) != 0:
                                coach = upper
                                berth_preference = 'UPR'
                            else:
                                return Response({'error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)  
                else:
                    upper = self.check_upper()
                    if len(upper) != 0:
                        coach = upper 
                        berth_preference = 'UPR'
                    else:
                        mid = self.check_mid()
                        if len(mid) != 0:
                            coach = mid
                            berth_preference = 'MID'
                        else:                    
                            lower = self.check_lower()
                            if len(lower) != 0:
                                coach = lower
                                berth_preference = 'LWR'
                            else:
                                return Response({'error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST) 
                data = {'name': name, 'age': age, 'gender':gender, 'coach':coach, 'berth_preference':berth_preference, 'ticket_type':ticket_type}
            else:
                data = {'name': name, 'age': age, 'gender':gender, 'child': True}     
            
            if data:
                serializer = PassengerSerializer(data=data)
                if serializer.is_valid():
                    ticket = serializer.save()               
                    data = {'url': reverse_lazy('ticket_status', args=[ticket.id])}  
                    return Response(data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            else:
                return Response({'error': 'Form data are empty'}, status=status.HTTP_400_BAD_REQUEST) 
        else:
            return Response({'error': 'No tickets available'}, status=status.HTTP_400_BAD_REQUEST) 
                    
    def check_lower(self):
        coach = False
        if self.s1_cnt < 8 and self.s1_lower < 3:
            coach = 'S1'
        elif self.s2_cnt < 8 and self.s2_lower < 3:
            coach = 'S2'
        elif self.s3_cnt < 8 and self.s3_lower < 3:
            coach = 'S3'
        elif self.s4_cnt < 8 and self.s4_lower < 3:
            coach = 'S4'
        return coach

    def check_mid(self):
        coach = False
        if self.s1_cnt < 8 and self.s1_mid < 2:
            coach = 'S1'
        elif self.s2_cnt < 8 and self.s2_mid < 2:
            coach = 'S2'
        elif self.s3_cnt < 8 and self.s3_mid < 2:
            coach = 'S3'
        elif self.s4_cnt < 8 and self.s4_mid < 2:
            coach = 'S4'
        return coach

    def check_upper(self): 
        coach = False       
        if self.s1_cnt < 8 and self.s1_upper < 3:
            coach = 'S1'
        elif self.s2_cnt < 8 and self.s2_upper < 3:
            coach = 'S2'
        elif self.s3_cnt < 8 and self.s3_upper < 3:
            coach = 'S3'
        elif self.s4_cnt < 8 and self.s4_upper < 3:
            coach = 'S4'
        return coach

class TicketStatus(APIView):
    def get(self, request, pk): 
        passenger = Passenger.objects.get(pk=pk)
        gender = Gender.objects.get(code=passenger.gender)  
        print('@@@@')
        print(passenger.child)
        print(passenger.coach)
        if passenger.child == True:
           coach = berth = ticket_type = None
           msg ='The tickets should not be allocated for children below age 5' 
           #label = 'text-warning'
           label = False
        else: 
            try:
                coach = Coach.objects.get(code=passenger.coach).name
            except Coach.DoesNotExist:
                coach = None

            try:
                berth = Berth.objects.get(code=passenger.berth_preference).name
            except Berth.DoesNotExist:
                berth = None

            try:
                ticket_type = TicketType.objects.get(code=passenger.ticket_type).name
            except TicketType.DoesNotExist:
                ticket_type = None
            msg = 'Ticked booked successfully' 
            label = True
            #label = 'text-success'
        date = datetime.strftime(passenger.created_at,"%d-%m-%Y %H:%M:%S")   
        
        data = {
            'id' : 'T-'+ str(passenger.id),
            'name' : passenger.name,
            'age' : passenger.age,
            'gender' : gender.name,
            'coach' : coach,
            'berth' : berth,
            'ticket_status' : ticket_type,
            'created_at' : date,            
            'msg': msg,
            'label': label,
        }
        return Response(data)

class PasengerList(APIView):
    def get(self, request):
        passenger = Passenger.objects.all()
        data = PassengerSerializer(passenger, many=True).data
        return Response(data)


