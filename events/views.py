from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event


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
