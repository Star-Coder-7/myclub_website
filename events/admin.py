from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event

# admin.site.register(Venue, VenueAdmin)
admin.site.register(MyClubUser)
# admin.site.register(Event)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'eventDate', 'description', 'manager')
    list_display = ('name', 'eventDate', 'venue')
    list_filter = ('eventDate', 'venue')
    ordering = ('eventDate',)
