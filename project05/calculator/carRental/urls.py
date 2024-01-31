from . import views
from django.urls import path,include

app_name='carRental'

urlpatterns=[
    path('',views.mainRentCarView,name='mainRent'),
    path('/cars',views.CarsView,name='cars'),
    path('/pricing',views.PricingView.as_view(),name='pricing'),
    path('/faq',views.FaqView,name='faq'),
    path('/opinions',views.opinionView,name='opinions'),
    path('/book',views.bookView,name='book'),
    path('/successful',views.succesView,name='successful'),
    
    

    
]