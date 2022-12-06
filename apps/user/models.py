from django.db import models
from apps.account.models import User
# Create your models here.
class Address(models.Model):
    to = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=20)
    short_address = models.CharField(max_length=120)
    no = models.PositiveBigIntegerField()
    unit = models.PositiveBigIntegerField()
    zip_code = models.PositiveBigIntegerField()

    def __str__(self):
        return self.short_address + '-' + str(self.zip_code)

    @property
    def full_address(self):
        address = self.city + ',' + self.short_address + ',N.o ' + str(self.no) + ',Unit ' + str(self.unit)
        return address