from django.db import models


# Create your models here.
class tbl_District(models.Model):
    District_id = models.AutoField(primary_key=True)
    District_Name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.District_Name
    
class tbl_location(models.Model):
    Location_id = models.AutoField(primary_key=True)
    Ward_No= models.IntegerField()
    Ward_Name= models.CharField(max_length=100)
    District = models.ForeignKey(tbl_District, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Ward_Name
    
class tbl_residentsassociation(models.Model):
    RA_id = models.AutoField(primary_key=True)
    Association_Name = models.CharField(max_length=200)
    Location = models.ForeignKey(tbl_location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Association_Name