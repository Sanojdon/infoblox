from django.db import models

# Create your models here.
class DataRead(models.Model):
    dr_id = models.IntegerField("ID")
    dr_fname = models.CharField("First Name", max_length=15)
    dr_lname = models.CharField("Last Name", max_length=15)
    dr_city = models.CharField("City", max_length=50, default="Bangalore")
    dr_data = models.TextField("Data", max_length=250, default="")

    def __str__(self):
        return self.dr_fname + " " + self.dr_lname

# id, first_name, last_name, city, data
