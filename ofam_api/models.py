from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Exhibition(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='Current Exhibition')
    start_date = models.DateField()
    end_date = models.DateField()
    archive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
