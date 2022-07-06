from django.shortcuts import render, get_object_or_404, redirect
from main.models import Loan, LoanCategory
from main.forms import UserForm, UserLoginForm, InvestorForm
from django.contrib.auth import login, authenticate, logout
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def index(request):
    template = "index.html"
    loan_listing = Loan.objects.all()
    top_listing = loan_listing.order_by('?')[:10]
    context = {'top_listing':top_listing}
    return render(request, template, context)


def about(request):
    template = "about.html"
    context = {}
    return render(request, template, context)

def tender_listings(request):
    loan_listing = Loan.objects.all()
    template = "tenders.html"
    context = {'loan_listing':loan_listing}
    return render(request, template, context)

def business_signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('loanapplication:business')
    else:
        form = UserForm()
    template = "signup.html"
    context = {'form':form}
    return render(request, template, context)

def individual_signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('loanapplication:individual')
    else:
        form = UserForm()
    template = "signup2.html"
    context = {'form':form}
    return render(request, template, context)

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            message = messages.info(request, f'account does not exit plz sign in')
            print(messages)
    form = UserLoginForm()
    template = "login.html"
    context = {'form':form}
    return render(request, template, context)

def logout_request(request):
    logout(request)
    return redirect("signin")

def investors(request):
    form = InvestorForm(request.POST or None)

    if form.is_valid():
        if request.method == "POST":
            form = InvestorForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                success = messages.success(request, ('Success!'))
                return redirect('loanapplication:lipa_na_mpesa')
            else:
                messages.error(request, 'Error saving form')

                return redirect("index")

            form = InvestorForm()
    template = "investors.html"
    context = {'form':form}
    return render(request, template, context)
