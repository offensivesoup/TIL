from django.db import models
from django.db.models import F

class Event(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    participants = models.ManyToManyField('Participant', through='Attendance')

    def __str__(self):
        return self.name

    def event_price(self):
        return self.price
    
class Participant(models.Model):
    name = models.CharField(max_length=100)
    num_of_participants = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)
    events = models.ManyToManyField('Event', through='Attendance')

    def __str__(self):
        return self.name

    def participant_num(self):
        return self.num_of_participants

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    check_in = models.TimeField()
    check_out = models.TimeField()
    total_fee = models.IntegerField()

    def __str__(self):
        return f'{self.participant} - {self.event}'
    
    def add(self, *args, **kwargs):
        self.total_fee = self.calcul()
        super().save(*args, **kwargs)
    
    def calcul(self):
        price = self.event.event_price()
        num = self.participant.participant_num()
        result = price * num
        return result