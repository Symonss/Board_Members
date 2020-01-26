from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

class Institutional(models.Model):
    name = models.CharField(max_length = 100)
    

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length = 100)
        
    def __str__(self):
        return self.name


#
class Member(models.Model):
    STATUS_CHOICES = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
    )
    name = models.CharField(max_length=100)
    institutional = models.ForeignKey(Institutional, on_delete = models.CASCADE)
    position = models.ForeignKey(Position, on_delete = models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='1')
    appointment_schedule = models.CharField(max_length = 300)
    date_of_appointment = models.DateTimeField()
    date_of_expiry = models.DateTimeField()
    gazetted_by = models.CharField(max_length = 100)
    is_expired = models.BooleanField(default = False)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('post_detail_view', args=[self.slug])
