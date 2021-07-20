from django.shortcuts import render, redirect
from django.http import Http404
from .models import user, investment


# Create your views here.
def home(request):
    return render(request, 'home.html')


def reguser(request):
    return render(request, 'reguser.html')


def registeruserafter(request):
    typeofuser = request.POST['typeofuser']
    username = request.POST['inputUsername']
    fisrtname = request.POST['inputFirstName']
    middlename = request.POST['inputMiddleName']
    lastname = request.POST['inputLastName']

    contactno = request.POST['inputcontactno']

    email = request.POST['inputEmail3']
    password = request.POST['inputPassword']

    gender = request.POST['inputGender']
    city = request.POST['inputCity']
    state = request.POST['inputState']
    country = request.POST['inputCountry']
    pincode = request.POST['inputPincode']

    t1 = user.objects.all().count()

    a = user(typeofuser=typeofuser, username=username, fname=fisrtname, mname=middlename, lname=lastname,
             contactno=contactno,
             emailid=email, password=password, gender=gender,
             city=city, state=state, country=country, pincode=pincode)
    a.save()

    t2 = user.objects.all().count()

    if t2 == t1 + 1:
        error = "User Registered Succesfully!!"
    return render(request, 'reguser.html', {'error': error})


def login(request):
    return render(request, 'login.html')


def loginafter(request):
    username = request.POST['inputUsername']
    password = request.POST['inputPassword']

    try:

        auth_user = user.objects.all().filter(username=username, password=password).count()

        if auth_user == 1:
            obj = user.objects.all().get(username=username)
            value = obj.typeofuser

            if value == "Investor":
                request.session['investor'] = "True"
                request.session['username'] = username
                return redirect('Invest/')
            else:
                request.session['borrower'] = "True"
                request.session['username'] = username
                return redirect('Borrower/')

        else:
            flage = 1
            return render(request, "login.html", {'error': "Please Enter Correct Combination of Usename and Password."})

    except:
        raise Http404("User is not Avaiable")


def Investor(request):
    username = request.session['username']
    if user.objects.all().filter(username=username).count() == 1:
        obj = investment.objects.all().filter(investor=username)
        return render(request, 'investor.html', {'data': obj})
    else:
        return render(request, 'investor.html', {'error': "You Are not Allowed to see that page."})


def updateinevstment(request):
    status = request.POST['status']

    username, status = status.split('-')
    obj = investment.objects.all().get(investor=request.session['username'], Borrower=username)
    if status == "Disinvest":
        obj.amount = 0
        obj.save()
    else:
        obj.amount = 0
        return render(request, 'investor.html', {'error': "You Are not Allowed to see that page."})


def update_investor(request):
    email = request.session['email']
    print(email)
    a = investment.objects.all().filter(email=email)
    return render(request, 'investor_update.html', {'data': a})


def update_investor_after(request):
    investor = request.POST['investor']
    Borrower = request.POST['Borrower']
    amount = request.POST['amount']
    date = request.POST['date']

    data2 = investment.objects.all().get(email='1@gmail.com')
    data2.investor = investor
    data2.Borrower = Borrower
    data2.amount = amount
    data2.date = date
    data2.save()

    data3 = investment.objects.all().filter(email='1@gmail.com')

    return render(request, 'investor_update.html', {'data': data3})
