from django.db import models


# Create your models here.
class user(models.Model):
    TYPE_CHOICES = (
        ('Investor', 'Investor'),
        ('Borrower', 'Borrower'),
    )
    typeofuser = models.CharField(max_length=10, choices=TYPE_CHOICES)
    username = models.CharField(max_length=100, primary_key=True)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    contactno = models.CharField(max_length=10)
    emailid = models.EmailField()
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.IntegerField()

    def __str__(self):
        return self.typeofuser + "  " + self.username


class investment(models.Model):
    investor = models.CharField(max_length=100)
    Borrower = models.CharField(max_length=100)
    amount = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.investor + "  " + self.Borrower + "  " + str(self.amount)
