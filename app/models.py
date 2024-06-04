from django.db import models

# Create your models here.


class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    founded = models.TextField(blank=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    length = models.IntegerField()
    stages = models.IntegerField()
    parking = models.BooleanField(default=False)
    kindergarden = models.BooleanField(default=False)
    elevators = models.BooleanField(default=False)




