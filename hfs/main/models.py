from django.db import models
import random
import string

def key_generator():
    key = ''.join(random.choice(string.digits) for x in range(6))
    if Loan.objects.filter(code=key).exists():
        key = key_generator()
    return key

# Create your models here.
class LoanCategory(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Loan Category"
        verbose_name_plural = "Loan Categories"

class Loan(models.Model):
    category = models.ForeignKey(LoanCategory, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    code = models.CharField(max_length=6, default=key_generator, unique=True, editable=False)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    active = models.BooleanField()
    description = models.TextField(max_length = 300)

    def __str__(self):
        return self.name

INVESTMENT_CHOICES = (
 ("Lender","Lender"),
 ("Private Investor","Private Investor"),
 ("Employer","Employer"),
)

class Investor(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    investment = models.CharField(null = True, blank = True, max_length = 250, choices = INVESTMENT_CHOICES, default = 'Lender')
    phone = models.CharField(max_length = 30)

    def __str__(self):
        return self.name
