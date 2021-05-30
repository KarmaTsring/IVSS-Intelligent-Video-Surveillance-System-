from django.db import models
import datetime

# Create your models here.


#Creating inheritance from models, "model.Model"
class Entries(models.Model):
    """create staff details table
    * each attributes with defnining size"""


    personNames = models.CharField(max_length=70, default='customers')
    person_post = models.CharField(max_length=50)
    personEntryTime = models.TimeField()

    #timeSpentStaff =



class Exits(models.Model):
    """create staff details table
    * each attributes with defnining size"""


    personNames = models.CharField(max_length=70)
    person_post = models.CharField(max_length=50)
    personExitTime = models.TimeField()









