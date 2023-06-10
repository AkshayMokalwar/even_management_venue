# from django.shortcuts import render

# Create your views here.

from datetime import datetime
import hashlib
# hashlib.sha256(a.encode('utf-8')).hexdigest()

from django.shortcuts import render ,redirect
from .models import Event, Venue, Booking,Organizer,End_User


# def create_events(request, organizer_id):
#     if request.method == 'POST':
#         organizer = Organizer.objects.get(id=organizer_id)
#         event_name = request.POST['event_name']
#         description = request.POST['description']
        
#         now = datetime.now() # current date and time
#         # YYYY-MM-DD
#         day = now.strftime("%Y-%m-%d")
#         print("day:", day)

#         time = now.strftime("%H:%M:%S")
#         print("time:", time)

#         event=Event(name=event_name,date=day,time=time,description=description,organizer=organizer)
#         event.save()
#         return render(request, 'event_detail.html', {'event': event})
#         # return render(request, 'booking_success.html', {'booking': booking})

#     else:
#         organizer = Organizer.objects.get(id=organizer_id)
#         return render(request, 'create_event.html', {'organizer': organizer})
# from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm

# from .forms import UserRegistrationForm
# from django.contrib import messages

def register(request):
    if request.method == 'POST':
        # event = Event.objects.get(id=event_id)
        # venue = Venue.objects.get(id=venue_id)
        customer_name = request.POST['customer_name']
        customer_password1 = hashlib.sha256(str(request.POST['customer_password1']).encode('utf-8')).hexdigest()
        customer_password = hashlib.sha256(str(request.POST['customer_password']).encode('utf-8')).hexdigest()
        customer_email = request.POST['customer_email']
        customer_organization = request.POST['customer_organization']
        customer_contact_details = request.POST['customer_contact_details']
        print()
        
        if(customer_password==customer_password1):

            now = datetime.now() # current date and time
            # YYYY-MM-DD
            day = now.strftime("%Y-%m-%d")
            print("day:", day)

            time = now.strftime("%H:%M:%S")
            print("time:", time)
            end_User = End_User(name=customer_name, contact_details=customer_contact_details, organization=customer_organization,email_id=customer_email,registration_date=day,registration_time=time,_password=customer_password)
            end_User.save()
            context = {'end_user': end_User}
            return render(request,'index.html',context)
        # return render(request, 'booking_success.html', {'end_User': end_User})
        # form = UserRegistrationForm(request.POST)
        # if form.is_valid():
        #     form.save()

        #     # messages.success(request, f'Your account has been created. You can log in now!')    
        #     return redirect('Home/')
        # context = {'form': form}
    return render(request, 'register.html')

def home_View(request):
    # redirect(request,'')
    if request.method == 'POST':
        email = request.POST['customer_email']
        # passward = request.POST['customer_password']
        passward=hashlib.sha256(str(request.POST['customer_password']).encode('utf-8')).hexdigest()
        print('email :',email)
        print('passward : ',passward)
        end_user=End_User.objects.filter(email_id=email)
        print('x'*10)
        for i in end_user:
            if(i.Authenticate_user(passward)):
                context = {'end_user': i}
                return render(request,'index.html',context)
    return render(request,'end_user_login.html')
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def venue_list(request):
    venues = Venue.objects.all()
    print('*'*10)
    # address = models.CharField(max_length=200)
    # capacity = models.PositiveIntegerField()
    # availability = models.BooleanField(default=True)
    for venue in venues:
        print(venue.name)
        print(venue.name)
        print(venue.name)

    return render(request, 'venue_list.html', {'venues': venues})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def venue_detail(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    
    return render(request, 'venue_detail.html', {'venue': venue})

def book_venue(request, event_id, venue_id):
    if request.method == 'POST':
        event = Event.objects.get(id=event_id)
        venue = Venue.objects.get(id=venue_id)
        customer_name = request.POST['customer_name']
        customer_email = request.POST['customer_email']

        booking = Booking(event=event, venue=venue, customer_name=customer_name, customer_email=customer_email)
        booking.save()
        return render(request, 'booking_success.html', {'booking': booking})

    else:
        event = Event.objects.get(id=event_id)
        print(event)
        venue = Venue.objects.get(id=venue_id)

        return render(request, 'book_venue.html', {'event': event, 'venue': venue})
    

def create_events(request, organizer_id):
    if request.method == 'POST':
        organizer = Organizer.objects.get(id=organizer_id)
        
        event_name = request.POST['event_name']
        description = request.POST['description']
        # name = models.CharField(max_length=100)
        # date = models.DateField()
        # time = models.TimeField()
        # description = models.TextField()
        # organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)

        now = datetime.now() # current date and time
        # YYYY-MM-DD
        day = now.strftime("%Y-%m-%d")
        print("day:", day)

        time = now.strftime("%H:%M:%S")
        print("time:", time)

        event=Event(name=event_name,date=day,time=time,description=description,organizer=organizer)
        event.save()
        return render(request, 'event_detail.html', {'event': event})
        # return render(request, 'booking_success.html', {'booking': booking})

    else:
        organizer = Organizer.objects.get(id=organizer_id)
        return render(request, 'create_event.html', {'organizer': organizer})

