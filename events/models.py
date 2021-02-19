from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zipCode = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Phone Number', max_length=25)
    web = models.URLField('Website Address')
    email = models.EmailField('Email Address')

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    eventDate = models.DateTimeField('Event Date and Time')
    # venue = models.CharField(max_length=120)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name

