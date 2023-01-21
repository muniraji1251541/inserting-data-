from django.db import models

# Create your models here.
class Sport(models.Model):
    sport_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.sport_name

class Player(models.Model):
    sport_name=models.ForeignKey(Sport,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name
    

class Detail(models.Model):
    name=models.ForeignKey(Player,on_delete=models.CASCADE)
    date=models.DateField()