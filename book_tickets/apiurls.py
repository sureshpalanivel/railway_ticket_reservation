from django.urls import path, include
from book_tickets.apiviews import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token

#VIEWSETS
# router = DefaultRouter()
# router.register('api/polls-viewset', PollViewSet)

urlpatterns = [ 
    path('form-data/', FormData.as_view(), name='api_form_data'),
    path('book/', BookTickets.as_view(), name='api_book_ticket'),
    path('status/<int:pk>/', TicketStatus.as_view(), name='api_ticket_status'),  

    #path('pasenger/list/', PasengerList.as_view(), name='pasenger_list'),

    #PURE DJ VIEWS
    #path('pasenger/list/', pasenger_list, name='pasenger_list'),
    #path('pasenger/list/', pasenger_list, name='pasenger_list'),
    # path('polls/<int:pk>/', polls_detail, name='polls_detail'),

    # #APIVIEWS
    # path('api/si/polls/', SimplePollList.as_view(), name='api_si_polls_list'),
    # path('api/si/polls/<int:pk>/', SimplePollsDetail.as_view(), name='api__si_polls_detail'),

    # #GENERIC VIEWS
    # path('api/polls/', PollList.as_view(), name='api_polls_list'),
    # path('api/polls/<int:pk>/', PollsDetail.as_view(), name='api_polls_detail'),
    # #path('api/polls/choices/', ChoiceList.as_view(), name='api_polls_choices'), #My
    # path('api/polls/<int:pk>/choices/', ChoiceList.as_view(), name='api_polls_choices'),
    # path('api/polls/choices/<int:pk>/', ChoiceDetail.as_view(), name='api_polls_detail'),
    # #path('api/polls/vote/', CreateVote.as_view(), name='api_polls_vote'), #My
    # path('api/polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='api_polls_vote'),
    # path('api/polls/vote/list/', VoteList.as_view(), name='api_polls_vote_list'),
    # path('api/polls/vote/<int:pk>/', VoteDetail.as_view(), name='api_polls_vote_detail'),
    
    # #AccessControl
    # path('api/create/user/', UserCreate.as_view(), name='api_create_user'),
    # path('api/login/', LoginView.as_view(), name='api_login'),
    # #path('api/login/', views.obtain_auth_token, name='api_login'),

    # path('', include(router.urls)),
    # #path('api-auth/', include('rest-framework.urls', namespace='rest_framework'))

    # ## NEW
    # path('api/example/view/', ExampleView.as_view(), name='api_example_view'),


    # #API AUTHTOKEN CHECK URL
    # #path('api/api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    # path('api/api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),  # <-- And here
]

#rlpatterns +=router.urls