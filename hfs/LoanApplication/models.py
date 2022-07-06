from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

LOANTYPE_CHOICES = (
    ("Poverty Reduction Support Loan", "Poverty Reduction Support Loan"),
    ("Investment Loan (Sacco)", "Investment Loan (Sacco)"),
    ("Agriculture/Farming Loan", "Agriculture/Farming Loan"),
    ("Business Loan", "Business Loan"),
    ("Church Support", "Church Support"),
    ("Schools/Learning Institutions", "Schools/Learning Institutions"),
    ("Mitigation assistance", "Mitigation assistance"),
    ("EIDL Advance Programs", "EIDL Advance Programs"),
    ("Microloan", "Microloan"),
)

ORGANIZATION_CHOICES = (
    ("Limited Liability Company", "Limited Liability Company"),
    ("Sole Proprietorship", "Sole Proprietorship"),
    ("C-Corporation", "C-Corporation"),
    ("S-Corporation", "S-Corporation"),
    ("General Patnership", "General Patnership"),
    ("Limited Liability Patnership", "Limited Liability Patnership"),
    ("Limited Partnership", "Limited Partnership"),
    ("Cooperative", "Cooperative"),
    ("Trust", "Trust"),
    ("Self-help Group", "Self-help Group"),
    ("Independent Contractor", "Independent Contractor"),
    ("Other", "Other"),
)

ACTIVITY_CHOICES = (
    ("Agriculture", "Agriculture"),
    ("Automotive Repair", "Automotive Repair"),
    ("Automotive Sales & Gas Service Stations", "Automotive Sales & Gas Service Stations"),
    ("Business Services", "Business Services"),
    ("Communications", "Communications"),
    ("Constructions & Contractors", "Constructions & Contractors"),
    ("Restaurants", "Restaurants"),
    ("Educational Services", "Educational Services"),
    ("Entertainment Services", "Entertainment Services"),
    ("Educational/Scientific Research", "Educational/Scientific Research"),
    ("Finance", "Finance"),
    ("Food & Beverage Stores", "Food & Beverage Stores"),
    ("Freight", "Freight"),
    ("Health Services", "Health Services"),
    ("Insurance", "Insurance"),
    ("Legal Services", "Legal Services"),
    ("Manufacturing", "Manufacturing"),
    ("Mining & Ntural Resource Extraction", "Mining & Ntural Resource Extractio"),
    ("Miscellaneous Services", "Miscellaneous Services"),
    ("Other", "Other"),
)

PAYMENT_CHOICES = (
    ("Nonrefundable grant", "Nonrefundable grant"),
    ("3 months", "3 months"),
    ("6 months", "6 months"),
    ("1 year", "1 year"),
    ("18 months", "18 months"),
    ("2 years", "2 years"),
    ("3 years", "3 years"),
    ("4 years", "4 years"),
    ("5 years", "5 years"),
    ("6 years", "6 years"),
    ("7 years", "7 years"),
    ("8+ years", "8+ years"),
)



class BusinessLoan(models.Model):
    user = models.ForeignKey(User, default = 1, null = True, on_delete = models.CASCADE)
    loanType = models.CharField(null = True, blank = True, max_length = 250, choices = LOANTYPE_CHOICES, default = 'Poverty Reduction Support Loan')
    businessDesc = models.CharField(null = True, blank = True, max_length = 500)
    loanReq = models.CharField(null = True, blank = True, max_length = 500)
    Names = models.CharField(null = True, blank = True, max_length = 500)
    BusinessNumber = models.IntegerField(null = True, blank = True )
    NonProfit = models.CharField(null = True, blank = True, max_length = 500)
    Franchise = models.CharField(null = True, blank = True, max_length = 500)
    organization = models.CharField(null = True, blank = True, max_length = 150, choices = ORGANIZATION_CHOICES, default = 'Sole Proprietorship')
    activity = models.CharField(null = True, blank = True, max_length = 150, choices = ACTIVITY_CHOICES, default = 'Agriculture')
    detActivity = models.TextField(null = True, blank = True, max_length = 5000)
    branches = models.IntegerField(null = True, blank = True)
    employees = models.IntegerField(null = True, blank = True, )
    PrimarySOI = models.CharField(null = True, blank = True, max_length = 500)
    GrossIncome = models.IntegerField(null = True, blank = True, )
    AdditionalSOI = models.CharField(null = True, blank = True, max_length = 500)
    MonthExp = models.IntegerField(null = True, blank = True)
    StartDate = models.DateField(null = True, blank = True)
    BusinessPhone = models.CharField(null = True, blank = True, max_length = 500)
    AlternativePhone = models.CharField(null = True, blank = True, max_length = 500)
    BusinessEmail = models.EmailField(null = True, blank = True)
    BusinessWeb = models.CharField(null = True, blank = True, max_length = 500)
    BusinessAddress = models.CharField(null = True, blank = True, max_length = 500)
    OwnerName = models.CharField(null = True, blank = True, max_length = 500)
    PercOfOwn = models.IntegerField(null = True, blank = True)
    Phone = models.CharField(null = True, blank = True, max_length = 500)
    email = models.EmailField(null = True, blank = True)
    Amount = models.IntegerField(null = True, blank = True)
    Purpose = models.CharField(null = True, blank = True, max_length = 500)
    information = models.TextField(null = True, blank = True, max_length = 500)
    paymentplan = models.CharField(null = True, blank = True, max_length = 500)
    desBank = models.CharField(null = True, blank = True, max_length = 500)
    accNumber = models.CharField(null = True, blank = True, max_length = 500)
    regFee = models.IntegerField(null = True, blank = True)
    VAT = models.IntegerField(null = True, blank = True)
    ExciseDuty = models.IntegerField(null = True, blank = True)
    total = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return self.Names

    @property
    def ccVAT(self):
        self.VAT = float(self.Amount) * float(0.0519)
        return round(self.VAT,2)

    @property
    def ccExciseduty(self):
        self.ExciseDuty = float(self.Amount) * float(0.0498)
        return round(self.ExciseDuty,2)

    @property
    def ccregFee(self):
        self.regFee = float(self.Amount) * float(0.100)
        return round(self.regFee,2)

    @property
    def ccTotal(self):
        self.total = self.ccregFee + self.ccExciseduty + self.ccVAT
        return round(self.total,2)

AGR_CHOICES = (
  ("Applicant is not engaged in any illegal activity (as defined by Federal guidelines).","Applicant is not engaged in any illegal activity (as defined by Federal guidelines)."),
  ("Applicant is not into gambling activities both legal and illegal.","Applicant is not into gambling activities both legal and illegal."),
  ("Applicant is not in the business of lobbying.","Applicant is not in the business of lobbying."),
  ("Is an adult of sound mind.","Is an adult of sound mind."),
  ("Holds a valid government issued form of identity.","Holds a valid government issued form of identity."),
  ("Is a citizen, resident or holds a valid visa for the country of residence.","Is a citizen, resident or holds a valid visa for the country of residence."),
)

EMPLOYMENTST_CHOICES = (
 ("Unemployed","Unemployed"),
 ("Government Employee","Government Employee"),
 ("Full-Time Empoyee","Full-Time Empoyee"),
 ("Part-Time Employee","Part-Time Employee"),
 ("Independent contractor","Independent contractor"),
 ("Self Employed","Self Employed"),
)

FUNDSUSE_CHOICES = (
 ("Personal use","Personal use"),
 ("Non-Personal use","Non-Personal use"),
)

DISBURSEMENT_CHOICES = (
 ("Lampsum","Lampsum"),
 ("Milestone","Milestone"),
)

class IndividualLoan(models.Model):
    user = models.ForeignKey(User, default = 1, null = True, on_delete = models.CASCADE)
    loanType = models.CharField(null = True, blank = True, max_length = 250, choices = LOANTYPE_CHOICES, default = 'Poverty Reduction Support Loan')
    grant = models.CharField(null = True, blank = True, max_length = 50)
    loanReq = models.CharField(null = True, blank = True, max_length = 500)
    Names = models.CharField(null = True, blank = True, max_length = 200)
    idNumber = models.IntegerField(null = True, blank = True)
    loanCheck = models.CharField(null = True, blank = True, max_length = 100)
    employmentST = models.CharField(null = True, blank = True, max_length = 250, choices = EMPLOYMENTST_CHOICES, default = 'Unemployed')
    gmonthlyIncome = models.IntegerField(null = True, blank = True)
    phone = models.IntegerField(null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    address = models.CharField(max_length = 300, null = True, blank = True)
    Amount = models.IntegerField(null = True, blank = True)
    fundUse = models.CharField(max_length = 300, null = True, blank = True)
    detFundUse = models.TextField(max_length = 1000, null = True, blank = True)
    paymentplan = models.CharField(null = True, blank = True, max_length = 500)
    additionalinfo = models.TextField(max_length = 1000, null = True, blank = True)
    disbursement = models.CharField(null = True, blank = True, max_length = 250, choices = DISBURSEMENT_CHOICES, default = 'Milestone')
    desBank = models.CharField(null = True, blank = True, max_length = 500)
    accNumber = models.CharField(null = True, blank = True, max_length = 500)

    def __str__(self):
        return self.Names

    @property
    def ccVAT(self):
        self.VAT = float(self.Amount) * float(0.0519)
        return round(self.VAT,2)

    @property
    def ccExciseduty(self):
        self.ExciseDuty = float(self.Amount) * float(0.0498)
        return round(self.ExciseDuty,2)

    @property
    def ccregFee(self):
        self.regFee = float(self.Amount) * float(0.100)
        return round(self.regFee,2)

    @property
    def ccTotal(self):
        self.total = self.ccregFee + self.ccExciseduty + self.ccVAT
        return round(self.total,2)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# M-pesa Payment models
class MpesaCalls(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Call'
        verbose_name_plural = 'Mpesa Calls'


class MpesaCallBacks(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = 'Mpesa Call Back'
        verbose_name_plural = 'Mpesa Call Backs'

class MpesaPayment(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.TextField()
    organization_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'
    def __str__(self):
        return self.first_name
