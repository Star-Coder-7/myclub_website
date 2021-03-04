from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event
from .forms import VenueForm


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})


def allEvents(request):
    eventList = Event.objects.all()
    return render(request, 'events/event_list.html', {'eventList': eventList})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Shiven"
    month = month.capitalize()
    # Convert month from name to number
    monthNumber = list(calendar.month_name).index(month)
    monthNumber = int(monthNumber)

    # Create a calendar
    cal = HTMLCalendar().formatmonth(year, monthNumber)

    # Get the current year
    now = datetime.now()
    currentYear = now.year

    # get the time
    time = now.strftime('%d/%m/%Y, %H:%M:%S %p')

    return render(request, 'events/home.html', {
        "name": name,
        "year": year,
        "month": month,
        "month_number": monthNumber,
        "cal": cal,
        "current_year": currentYear,
        "time": time,
    })
