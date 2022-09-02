from django.db import models

# Create your models here.

class Fruit(models.Model):
    Name=models.CharField(max_length=100)
    Qunatity=models.IntegerField()
    Calories=models.IntegerField()
    Fat=models.FloatField()
    Sodium=models.IntegerField()
    Potasium=models.IntegerField()
    Carbohydrates=models.IntegerField()
    Dietary_Fiber=models.IntegerField()
    Sugars=models.IntegerField()
    Protein=models.IntegerField()
    Image=models.ImageField(upload_to="image",default=" ")
