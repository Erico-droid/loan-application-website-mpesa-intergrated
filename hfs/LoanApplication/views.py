from django.shortcuts import render, redirect
from LoanApplication.forms import BusinessLoanForm, IndividualLoanForm
from django.contrib import messages
from LoanApplication.models import BusinessLoan, IndividualLoan
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import time
from requests.auth import HTTPBasicAuth
import requests
from .mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment, IndividualLoan, BusinessLoan
import json

# Create your views here.
@login_required(login_url='signin')
def individual(request):
    form = IndividualLoanForm(request.POST or None)

    if form.is_valid():
        if request.method == "POST":
            form = IndividualLoanForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                success = messages.success(request, ('Your Loan application was successfully received!'))
                return redirect('loanapplication:creditchecker')
            else:
                messages.error(request, 'Error saving form')

                return redirect("index")

            form = IndividualLoanForm()
    list = IndividualLoan.objects.all()
    template = 'loan2.html';
    context = {'form':form,'list':list}
    return render(request, template, context)

@login_required(login_url='signin')
def business(request):
    # create object of form
    form = BusinessLoanForm(request.POST or None)

    # check if form data is valid
    if form.is_valid():
        if request.method == "POST":
            form = BusinessLoanForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                success = messages.success(request, ('Your Loan application was successfully received!'))
                return redirect('loanapplication:creditchecker')
            else:
                messages.error(request, 'Error saving form')

                return redirect("index")

            form = BusinessLoanForm()

    template = 'loan.html';
    context = {'form':form}
    return render(request, template, context)

@login_required(login_url='signin')
def creditchecker(request):
    template = 'creditchecker.html'
    context = {}
    return render(request, template,context)


def getAccessToken(request):
    consumer_key = '4A9Qvlj99deGpDyDDHRnA9JCdAWxmyjs' #copy hfs consumer key
    consumer_secret = '9m2vjCRX0I3TeyFj' #copy hfs consumer secret
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)

@login_required(login_url='signin')
def lipa_na_mpesa_online(request):
    response_data = {}
    current_user = request.user
    queryset = IndividualLoan.objects.filter(user = request.user.id)
    if queryset.exists():
        queryset = IndividualLoan.objects.get(user = request.user.id)
    else:
        queryset = BusinessLoan.objects.get(user = request.user.id)
    print(queryset)
    if request.POST.get('action') == 'ajax-post':
        MpesaNo = request.POST.get('mpesaNumber')
        response_data['message'] = "Check your phone for ussd prompt to complete the payment."
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerBuyGoodsOnline",
            "Amount": queryset.ccTotal,
            "PartyA": MpesaNo,  # replace with your phone number to get stk push
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": MpesaNo,  # replace with your phone number to get stk push
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Kijana",
            "TransactionDesc": "Get the money first."
        }
        response = requests.post(api_url, json=request, headers=headers)
        print(queryset)
        return JsonResponse(response_data)
    context = {'queryset':queryset}
    template = 'payment.html'
    return render(request, template, context)

@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization":"Bearer %s" % access_token}
    options = {"ShortCode":LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType":"Completed",
               "ConfirmationURL":"https://6b0c-102-68-76-241.ngrok.io/loan-application/c2b/confirmation",
               "ValidationURL":"https://6b0c-102-68-76-241.ngrok.io/loan-application/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    # print(headers, options)
    return HttpResponse(response.text)

@csrf_exempt
def call_back(request):
    print(request)
    return HttpResponse(request)


@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
