from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

import html

from datetime import datetime, timedelta
#from django.template import loader

from .models import Users

def dumpdata(place, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

def index(request):
    users_list = Users.objects.all()
    #users_list = get_list_or_404(Users, pk!=NULL)
    #template = loader.get_template('fablab/index.html')
    context = {
        'users_list': users_list,
        }
    #return HttpResponse(template.render(context, request))
    return render(request, 'fablab/index.html', context)

def userdetails(request, user_id):
    return HttpResponse("You are looking at the details of user: %s" % user_id)

def booking(request, user_id):
    #user = Users.objects.get(pk=user_id)
    user = get_object_or_404(Users, pk=user_id)
    userBooking=user.booking_set.all()
    context = {
        'user': user,
        'userBooking':userBooking
    }
    return render(request, 'fablab/user_booking.html', context)

class BookingPage(View):
    def get(self, request):
        weekDays = []
        timeOfDay = []

        today = datetime.now().weekday() #Get today's date and the work out which day it is
        delta = timedelta(days=-today) # create the time delta that would count back to Monday
        monday = datetime.now() + delta # Adding the timedelta will bring us back to monday
        dayName = monday.date().strftime("%A")
        hour = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=9, minute=0)
        for i in range(5):
            theDay = []
            delta = timedelta(days=+i)
            day = monday + delta
            dayName = day.date().strftime("%A")
            theDay.append(dayName)
            theDay.append(day)
            weekDays.append(theDay)

        for i in range(9):
            deltaTime = timedelta(hours=+1)
            timeOfDay.append(hour.time)
            hour = hour + deltaTime

        context = {
            'weekDays': weekDays,
            'dayName': dayName,
            'timeOfDay': timeOfDay,
        }

        return render(request, 'fablab/booking.html', context)


class BookFablab(View):
    @csrf_exempt
    def get(self, request):
        user = get_object_or_404(Users, pk=1)
        context = {
            'user': user,
        }
        return render(request, 'fablab/book_fablab.html', context)

def request_booking(request):
    fName = request.POST['firstName']
    lName = request.POST['lastName']
    email = request.POST['email']
    resDate = request.POST['reservationDate']
    startTime = request.POST['timeFrom']
    endTime = request.POST['timeFrom']

    try:
        user = get_object_or_404(Users, firstName=fName)


    except (KeyError, Users.DoesNotExist):
        return render(request, 'fablab/book_fablab.html')
    else:
        booking = user.booking_set.all()
        context = {
            'firstName': user.surName,
        }
        return HttpResponseRedirect(reverse('fablab:confirm_booking'))

class ConfirmBooking(View):
    def get(self, request):
        user = get_object_or_404(Users, pk=1)
        user_id = user.id
        userBooking=user.booking_set.all()
        context = {
            'userBooking': userBooking,
            'user_id' : user_id,
        }
        return render(request, 'fablab/confirm.html', context)

class AboutFablab(View):
    def get(self, request):
        context = {}
        return render(request, 'fablab/about.html', context)

