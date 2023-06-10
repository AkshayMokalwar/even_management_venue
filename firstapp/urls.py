# manually created on 20230610
#by AKshay M

from django.urls import path
from firstapp import views


urlpatterns = [
    path('Home/', views.home_View, name='home_View'),
    path('register/', views.register, name='register_View'),
    path('create_events/<int:organizer_id>/', views.create_events, name='create_events'),
    path('events/', views.event_list, name='event_list'),
    path('venues/', views.venue_list, name='venue_list'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('venues/<int:venue_id>/', views.venue_detail, name='venue_detail'),
    path('events/<int:event_id>/venues/<int:venue_id>/book/', views.book_venue, name='book_venue')
]
