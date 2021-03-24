from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')

    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})


def list_venues(request):
    venueList = Venue.objects.all()
    return render(request, 'events/venue.html', {'venueList': venueList})


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
