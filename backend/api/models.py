from django.db import models


# Create your models here.
class Item(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    permanent_address = models.TextField()
    zip_code = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    civil_status = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bloodtype = models.CharField(max_length=10, blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)
    gsis = models.CharField(max_length=20, blank=True, null=True)
    pag_ibig_no = models.CharField(max_length=20, blank=True, null=True)
    philhealth = models.CharField(max_length=20, blank=True, null=True)
    sss = models.CharField(max_length=20, blank=True, null=True)
    tin = models.CharField(max_length=20, blank=True, null=True)
    agency_employee_no = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    employee_business = models.CharField(max_length=100, blank=True, null=True)
    business_address = models.CharField(max_length=100, blank=True, null=True)
   


    def __str__(self):
        return self.first_name
