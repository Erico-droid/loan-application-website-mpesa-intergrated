from django.contrib import admin
from LoanApplication.models import BusinessLoan, IndividualLoan, MpesaPayment
# Register your models here.

admin.site.register(BusinessLoan)
admin.site.register(IndividualLoan)
admin.site.register(MpesaPayment)
