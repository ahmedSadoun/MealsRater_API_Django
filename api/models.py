from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator , MaxValueValidator
# Create your models here.

class Meal(models.Model):
    title=models.CharField(max_length=32)
    description=models.TextField(max_length=360)
    def no_of_ratings(self):
        self.ratings=Rating.objects.filter(meal=self.id)
        return len(self.ratings)
    
    def avg_rating(self):
        sum=0
        for x in self.ratings:
            sum+=x.stars
        if len(self.ratings) >0:
            return sum/len(self.ratings)
        else :
            return 0


    def __str__(self):
        return self.title

class Rating(models.Model):
    meal=models.ForeignKey(Meal, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)])
    # def __str__(self):
    #     return self.meal
    #the user can rate a meal just one time ,the next time an elegant error is being thrwon 
    class Meta:
        unique_together=(('user','meal'),)
        index_together=(('user','meal'),)


