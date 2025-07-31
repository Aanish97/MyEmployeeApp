from django.db import models
from user.models import User


class AddressType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    photo = models.ImageField(upload_to='employee_photos/')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Address(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='addresses')
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address_type.name} for {self.employee}"
