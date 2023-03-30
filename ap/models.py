from django.db import models

# Create your models here.

class Team(models.Model):
    Game=models.CharField(max_length=100,primary_key=True)

class Player(models.Model):
    Game=models.ForeignKey(Team,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

class Access(models.Model):
    name=models.ForeignKey(Player,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    