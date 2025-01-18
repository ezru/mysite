import datetime

from django.db import models
from django.utils import timezone

class Machines(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Users(models.Model):
    firstName = models.CharField(max_length=60)
    surName = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    created = models.DateTimeField(auto_now_add= True)
    bookMachine = models.ManyToManyField(Machines, through='Booking')

    def __str__(self):
        return self.firstName
    def was_added_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

class Items(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField('Description', max_length=300)
    quantity = models.IntegerField()
    loans = models.ManyToManyField(Users, through='ItemLoan')

    def __str__(self):
        return self.itemName

class ItemLoan(models.Model):
    user = models.ForeignKey(Items, on_delete=models.CASCADE)
    item = models.ForeignKey(Users, on_delete=models.CASCADE)
    loanDate = models.DateTimeField('borrowed_on')
    returnDate = models.DateTimeField('returned_on', null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Booking(models.Model):
    BOOKING_TYPE = (
        ('I', 'Individual'),
        ('G', 'Group'),
        )
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machines, on_delete=models.CASCADE)
    slotDate = models.DateField()
    slotStatTime = models.TimeField()
    slotEndTime = models.TimeField()
    bookingType = models.CharField(max_length=300)
    groupSize = models.IntegerField()

    def __str__(self):
        return str(self.user)