from django.db import models


class AdLocation(models.Model):
    name = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AdSpend(models.Model):
    location = models.ForeignKey(AdLocation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


class BusinessCrypto(models.Model):
    location = models.ForeignKey(AdLocation, on_delete=models.CASCADE)
    crypto_acquired = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
