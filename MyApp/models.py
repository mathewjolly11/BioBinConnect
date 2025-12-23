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


class tbl_Route(models.Model):
    Route_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(tbl_location, on_delete=models.CASCADE)
    residents_association = models.ForeignKey(tbl_residentsassociation, on_delete=models.CASCADE, null=True, blank=True)
    start_house_no = models.IntegerField(null=True, blank=True, verbose_name="Start House No")
    end_house_no = models.IntegerField(null=True, blank=True, verbose_name="End House No")

    def __str__(self):
        base = self.name
        if self.start_house_no and self.end_house_no:
            base += f" (Houses {self.start_house_no}-{self.end_house_no})"
        return base


class tbl_CollectorAssignment(models.Model):
    Assign_id = models.AutoField(primary_key=True)
    collector = models.ForeignKey('GuestApp.Collector', on_delete=models.CASCADE)
    Route_id = models.ForeignKey(tbl_Route, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.collector} - {self.Route_id} ({self.day_of_week})"

