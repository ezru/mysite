from django.db import models

class Catagories(models.Model):
    categ_name = models.CharField(max_length=250)
    description = models.CharField(max_length=300)
    categ_type = models.CharField('categoy type', max_length=100)

class Budget(models.Model):
    catagory = models.ForeignKey(Catagories, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    frequency = models.CharField(max_length=50)

class Transactions(models.Model):
    trans_date = models.DateTimeField("transaction date")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=300)
