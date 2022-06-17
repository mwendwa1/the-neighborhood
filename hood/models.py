from django.db import models



# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    location = models.CharField()



class User(models.Model):
    name = models.CharField()
    email = models.CharField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)



class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField()
    business_email = models.CharField()
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.save()
        self.delete()

    