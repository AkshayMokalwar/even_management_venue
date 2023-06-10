from django.contrib import admin

# Register your models here.


from .models import Booking,Event,Venue,Organizer,End_User

admin.site.register(Booking)

admin.site.register(Event)

admin.site.register(Venue)
admin.site.register(Organizer)


admin.site.register(End_User)