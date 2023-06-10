from django.db import models

# Create your models here.
# from django.db import models

class End_User(models.Model):
    # 256
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    email_id= models.EmailField()
    registration_date = models.DateField()
    registration_time = models.TimeField()
    _password=models.CharField(max_length=256)
    # calss.__setitem__(('fname','lname','val'),['m','kk','','KKKK'])
    # to update the class Field as required 
    def __setitem__(self, k, v):
        self.__dict__.update(zip(k, v) if type(k) is tuple else [(k, v)])
        
    def Authenticate_user(self, val_password):
        if(val_password==self._password):
            return True
        return False
    
    def set_password(self, val_password):
        self._password=val_password
    
    
    
class Organizer(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)

    def _str_(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)

    def _str_(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def _str_(self):
        return f'{self.event.name} - {self.venue.name}'
