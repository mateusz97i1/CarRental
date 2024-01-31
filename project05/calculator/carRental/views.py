from django.shortcuts import render
from django.shortcuts import redirect,render
from django.views.generic import TemplateView,FormView
from .forms import RentForm,CarForm,FaqForm,RateUSForm
from datetime import datetime
from django.db.models import Q
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from .models import RentCarModel,CarModel,RateUSModel

# Create your views here.
def mainRentCarView(request):
    
    form=RentForm(request.POST)
   

    if request.method=='POST':
       
        car_brand = request.POST.get('carBrand')
        from_date = request.POST.get('fromDate')
        to_date = request.POST.get('toDaate')

        request.session['car_brand'] = car_brand
        request.session['from_date'] = from_date
        request.session['to_date'] = to_date


        return redirect('carRental:book')
    
    context={
        'form':form,
       
    }


    return render(request,'mainRentCar.html',context=context)


def CarsView(request):
 return render(request,'carsView.html')

class PricingView(TemplateView):
    template_name='pricing.html'


def FaqView(request):
 
    form=FaqForm(request.POST)
 

    if request.method=='POST':
        form.save()

        return redirect('carRental:mainRent')


    context={

        'form':form

    }


    return render(request,'faq.html',context=context)

def opinionView(request):
   

    form=RateUSForm(request.POST)
    commentsFromModel=RateUSModel.objects.all().order_by('-date')

    if request.method=="POST":
        if form.is_valid():
            form.save()

            return redirect('carRental:opinions')

   
    context={

        'form':form,
        'opinion':commentsFromModel

    }

    return render(request,'opinions.html',context=context)

def bookView(request):

    
    form=RentForm(request.POST)

    car_brand_id = request.session.get('car_brand', '')
    from_date = request.session.get('from_date', '')
    to_date = request.session.get('to_date', '')

    initial_data = {
        'carBrand': car_brand_id,
        'fromDate': from_date,
        'toDaate': to_date,
    }


    rentFormInitial= RentForm(initial=initial_data)


    if request.method=='POST':
        

        if form.is_valid():

            car_brand_instance = CarModel.objects.get(pk=car_brand_id)

            overlapping_bookings = RentCarModel.objects.filter(
                        carBrand=car_brand_id,
                        fromDate=to_date,
                        toDaate=from_date
                    )

            RentCarModel.objects.create(
                fullName=form.cleaned_data['fullName'],
                country=form.cleaned_data['country'],
                idNumber=form.cleaned_data['idNumber'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                carBrand=car_brand_instance,
                fromDate=form.cleaned_data['fromDate'],
                toDaate=form.cleaned_data['toDaate'],
                otheText=form.cleaned_data['otheText'],
            )
        if not form.is_valid():
            print(form.errors)


        return redirect('carRental:successful')

    context={

       'form':rentFormInitial,

    }
   

    return render(request,'book.html',context=context)



def succesView(request):

    if request.method=="POST":

        return redirect('carRental:mainRent')

    return render( request,'successful.html')