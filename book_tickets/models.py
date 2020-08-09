from django.db import models

# Create your models here.

# class OrdproxyManager(models.Manager):
#     # def get_queryset(self):
#     #     return super().get_queryset().filter(product__price__lte = '10')

#     # def all_objects(self):
#     #     return super().get_queryset()

#     def tickets_count(self):
#         return super().get_queryset().count()
#         # self.all_objects().filter(status = 'Out of Delivery') 

class Passenger(models.Model):   
    name = models.CharField(max_length=60)
    age = models.IntegerField()
    gender = models.CharField(max_length=6)
    child = models.BooleanField(default=False)
    coach = models.CharField(max_length=6, null=True, blank=True)    
    berth_preference = models.CharField(max_length=6, null=True, blank=True)
    ticket_type = models.CharField(max_length=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #objects = OrdproxyManager() 

    def __str__(self):
        return "{0} ({1})".format(self.name, self.id)

    # @property
    # def s1_count(self):
    #     return self.count()

    # @property
    # def tickets_count(self):
    #     return self.count()

    # @property
    # def tickets_count(self):
    #     return self.filter(coach = 'S1', ticket_type = 'CF').count()

class Gender(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.code)

class Coach(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.code)

class Berth(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.code)

class TicketType(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=36)

    def __str__(self):
        return "{0} ({1})".format(self.name, self.code)


# class PassengerDetails(models.Model):
#     GENDER_CHOICES = (
#         ('MA','Male'),
#         ('FM','Female'),
#     )

#     COACH_CHOICES = (
#         ('S1','S1'),
#         ('S2','S2'),
#         ('S3','S3'),
#         ('S4','S4'),
#     )

#     BERTH_CHOICES = (
#         ('UPR','Upper'),
#         ('LWR','Lower'),
#         ('MID','Middle'),
#         ('SID','Side Portion'),
#     )

#     TICKET_CHOICES = (
#         ('CF','Confirm'),
#         ('RAC ','Reservation Against Cancellation'),
#         ('WL','Waiting List'),
#     )

#     name = models.CharField(max_length=60)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
#     coach = models.CharField(max_length=50,choices=COACH_CHOICES)    
#     berth_preference = models.CharField(max_length=50,choices=BERTH_CHOICES)
#     ticket_type = models.CharField(max_length=50,choices=TICKET_CHOICES)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name