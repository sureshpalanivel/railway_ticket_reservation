from rest_framework import serializers
from rest_framework.authtoken.models import Token
from book_tickets.models import *
#from django.contrib.auth.models import User

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

class BerthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berth
        fields = '__all__'

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'


# HINTS
# Purpose of serializers
# Ex: Pollserializer class has a number of methods,
# is_valid(self, ..), create(self, validated_data, ..), update(self, instance, validated_data, ..), save(self, ..)

# poll_serializer = PollSerializer()
# print(repr(poll_serializer))
# poll_serializer = PollSerializer(data={'question':'what?', 'created_by':1})
# poll_serializer.is_valid()
# poll_serializer.validated_data
# poll_serializer.is_valid()
# poll = poll_serializer.save()
# poll.id
# poll_serializer.update(instance=poll, data={'question':'What is NexT?', 'created_by':1})


# class VoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vote
#         fields = '__all__'

# class ChoiceSerializer(serializers.ModelSerializer):
#     #votes = VoteSerializer(many=True, required=False)

#     class Meta:
#         model = Choice
#         fields = '__all__'

# class PollSerializer(serializers.ModelSerializer):
#     #choices = ChoiceSerializer(many=True, read_only=True, required=False)

#     class Meta:
#         model = Poll
#         fields = '__all__'



# class UserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ['username','email','password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User(username=validated_data['username'], email=validated_data['email'])
#         user.set_password(validated_data['password'])
#         user.save()
#         Token.objects.create(user=user)
#         return user
