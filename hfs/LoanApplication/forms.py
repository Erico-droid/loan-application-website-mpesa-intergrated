from django import forms
from .models import BusinessLoan, IndividualLoan
from django.forms.widgets import NumberInput

LOANTYPE_CHOICES = [
    ("Poverty Reduction Support Loan", "Poverty Reduction Support Loan"),
    ("Investment Loan (Sacco)", "Investment Loan (Sacco)"),
    ("Agriculture/Farming Loan", "Agriculture/Farming Loan"),
    ("Business Loan", "Business Loan"),
    ("Church Support", "Church Support"),
    ("Schools/Learning Institutions", "Schools/Learning Institutions"),
    ("Mitigation assistance", "Mitigation assistance"),
    ("EIDL Advance Programs", "EIDL Advance Programs"),
    ("Microloan", "Microloan"),
]

BUSINESSDESC_CHOICES = [
    ("applicant is an individual who operates under a sole proprietorship, with or without employees, or as an independent contractor.", "applicant is an individual who operates under a sole proprietorship, with or without employees, or as an independent contractor."),
    ("applicant is a small start-up business with less than 50 employees", "applicant is a small start-up business with less than 50 employees"),
    ("Applicant is an existing business with not more than 100 employees.", "Applicant is an existing business with not more than 100 employees."),
    ("Applicant is a corporate with not more than 500 employees", "Applicant is a corporate with not more than 500 employees"),
    ("Applicant is a private non-profit organization that is a non-governmental agency or entity with tax exemption", "Applicant is a private non-profit organization that is a non-governmental agency or entity with tax exemption"),
]

LOANREC_CHOICES = [
    ("Applicant is not engaged in any illegal activity (as defined by government guidelines)","Applicant is not engaged in any illegal activity (as defined by government guidelines)"),
    ("Does not derive more than a third of gross annual revenue from legal gambling activities.","Does not derive more than a third of gross annual revenue from legal gambling activities."),
    ("Applicant is not in the business of lobbying.","Applicant is not in the business of lobbying."),
    ("Applicant is compliant with country tax regulations","Applicant is compliant with country tax regulations"),
]

NONPROFIT_CHOICES = [
    ("Business is a Non-Profit Organization","Yes"),
    ("Business is not a Non-Profit Organization","No"),
]

FRANCHISE_CHOICES = [
    ("Business is a Franchise","Yes"),
    ("Business is not a Franchise","No"),
]

ORGANIZATION_CHOICES = [
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
]

ACTIVITY_CHOICES = [
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
]

PAYMENT_CHOICES = [
    ("Non-refundable grant", "Non-refundable grant"),
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
]

BANK_CHOICES = [
    ("Equity bank", "Equity bank"),
    ("Kenya Commercial Bank(KCB)", "Kenya Commercial Bank{KCB)"),
    ("Standard chartered bank", "Standard chartered bank"),
    ("Barclays Bank ", "Barclays Bank"),
    ("Cooperative Bank", "Cooperative Bank"),
    ("Diamond Trust Bank", "Diamond Trust Bank"),
    ("National Bank of Kenya", "National Bank of Kenya"),
    ("Stanbic Bank", "Stanbic Bank"),
]


class BusinessLoanForm(forms.ModelForm):
    loanType = forms.ChoiceField(choices=LOANTYPE_CHOICES)
    businessDesc = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style':'width:30px;list-style-type:none','required':'required'}), choices=BUSINESSDESC_CHOICES)
    loanReq = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'style':'width:30px;list-style-type:none','required':'required'}),choices=LOANREC_CHOICES,)
    Names = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Business Name','maxlength':100,'required':'required'}))
    BusinessNumber = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Business Number','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==10) return false;','required':'required'}))
    NonProfit = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style':'width:30px;list-style-type:none','required':'required'}), choices=NONPROFIT_CHOICES)
    Franchise = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style':'width:30px;list-style-type:none','required':'required'}), choices=FRANCHISE_CHOICES)
    organization = forms.ChoiceField(choices=ORGANIZATION_CHOICES)
    activity = forms.ChoiceField(choices=ACTIVITY_CHOICES)
    detActivity = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placeholder':'Minimum of two sentences','required':'required'}))
    branches = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'No. of branches','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==4) return false;','required':'required'}))
    employees = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'No. of employees','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==4) return false;','required':'required'}))
    PrimarySOI = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Primary source of income','required':'required'}))
    GrossIncome = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Monthly gross income in Kenya Shillings','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==9) return false;','required':'required'}))
    AdditionalSOI = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'maxlength':'1000','required':'required'}))
    MonthExp = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Monthly expenditure','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==9) return false;','required':'required'}))
    StartDate = forms.DateField(widget=NumberInput(attrs={'type':'date','required':'required'}))
    BusinessPhone = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'254 123 456 789','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==12) return false;','required':'required'}))
    AlternativePhone = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'254 123 456 789','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==12) return false;','required':'required'}))
    BusinessEmail = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'example@gmail.com','required':'required'}))
    BusinessWeb = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'www.example.com','required':'required'}))
    BusinessAddress = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'MaryPark Road, Westlands, Kenya','required':'required'}))
    OwnerName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Owner`s Name','required':'required'}))
    PercOfOwn = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Percantage of ownership','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==2) return false;','required':'required'}))
    Phone = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Personal phone number','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==12) return false;','required':'required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'example@gmail.com','required':'required'}))
    Amount = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Amount being applied for in Kenyan shillings','name':'amount','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==9) return false;','required':'required'}))
    Purpose = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'purpose of funding','required':'required'}))
    information = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'required':'required'}))
    paymentplan = forms.ChoiceField(choices=PAYMENT_CHOICES)
    desBank = forms.ChoiceField(choices=BANK_CHOICES)
    accNumber = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Selected bank account number','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==12) return false;','required':'required'}))
    class Meta:
        model = BusinessLoan
        exclude = ('user',)



AGR_CHOICES = [
  ("Applicant is not engaged in any illegal activity (as defined by Federal guidelines).","Applicant is not engaged in any illegal activity (as defined by Federal guidelines)."),
  ("Applicant is not into gambling activities both legal and illegal.","Applicant is not into gambling activities both legal and illegal."),
  ("Applicant is not in the business of lobbying.","Applicant is not in the business of lobbying."),
  ("Is an adult of sound mind.","Is an adult of sound mind."),
  ("Holds a valid government issued form of identity.","Holds a valid government issued form of identity."),
  ("Is a citizen, resident or holds a valid visa for the country of residence.","Is a citizen, resident or holds a valid visa for the country of residence."),
]

EMPLOYMENTST_CHOICES = [
 ("Unemployed","Unemployed"),
 ("Government Employee","Government Employee"),
 ("Full-Time Empoyee","Full-Time Empoyee"),
 ("Part-Time Employee","Part-Time Employee"),
 ("Independent contractor","Independent contractor"),
 ("Self Employed","Self Employed"),
]

FUNDSUSE_CHOICES = [
 ("Personal use","Personal use"),
 ("Non-Personal use","Non-Personal use"),
]

DISBURSEMENT_CHOICES = [
 ("Lampsum","Lampsum"),
 ("Milestone","Milestone"),
]

GRANT_CHOICES = [
 ("Non-refundable grant","Non-refundable grant"),
 ("Refundable loan","Refundable loan"),
]

LOANCHECK_CHOICES = [
    ("Applicant currently servicing a loan","Yes"),
    ("Applicant currently not servicing a loan","No"),
]

class IndividualLoanForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    loanType = forms.ChoiceField(choices=LOANTYPE_CHOICES)
    grant = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style':'width:30px;list-style-type:none','required':'required'}), choices=GRANT_CHOICES)
    loanReq = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'style':'width:30px;list-style-type:none','required':'required'}),choices=AGR_CHOICES,)
    Names = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Full names as per your ID','required':'required'}))
    idNumber = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'ID Number','required':'required','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==10) return false;'}))
    loanCheck = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style':'width:30px;list-style-type:none','required':'required'}), choices=LOANCHECK_CHOICES)
    employmentST = forms.ChoiceField(choices=EMPLOYMENTST_CHOICES)
    gmonthlyIncome = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'Gross monthly income in Kenya Shilings','required':'required','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==9) return false;'}))
    phone = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'254 701 234 567','required':'required','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==12) return false;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'example@gmail.com','required':'required'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'MaryPark Road, Westlands, Kenya','required':'required'}))
    Amount = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder':'In Kenya Shillings','required':'required','pattern':'/^-?\d+\.?\d*$/','onKeyPress':'if(this.value.length==9) return false;'}))
    fundUse = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'','required':'required'}))
    detFundUse = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'required':'required'}))
    paymentplan = forms.ChoiceField(choices=PAYMENT_CHOICES)
    additionalinfo = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'required':'required'}))
    disbursement = forms.ChoiceField(widget=forms.RadioSelect(attrs={'style':'width:30px;list-style-type:none','required':'required'}), choices=DISBURSEMENT_CHOICES)
    desBank = forms.ChoiceField(choices=BANK_CHOICES)
    accNumber = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder':'Selected bank account number','required':'required'}))
    class Meta:
        model = IndividualLoan
        exclude = ('user',)
