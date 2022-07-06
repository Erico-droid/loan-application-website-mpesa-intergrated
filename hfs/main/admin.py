from django.contrib import admin
from main.models import LoanCategory, Loan, Investor
# Register your models here.

admin.site.site_header = 'Haxe Financial Services(HFS)'
admin.site.site_title = "Haxe Financial Services(HFS) Administration"
admin.site.index_title = "Haxe Financial Services(HFS)"

admin.site.register(Loan)
admin.site.register(LoanCategory)
admin.site.register(Investor)
