from django.db import models
from django.contrib.auth.models import User

class Tournament(models.Model):

    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    game = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    country_restriction = models.CharField(max_length=50, null=True, blank=True)
    number_restriction = models.IntegerField(null=True, blank=True)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2)
    prize_pool = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Open', 'Open'), ('Closed', 'Closed')])
    participants = models.ManyToManyField(User, related_name='tournament_participants', blank=True)
    image = models.ImageField(upload_to='tournament_images/', null=True, blank=True) 

    def __str__(self):
        return self.title

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user