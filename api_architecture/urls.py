from django.urls import include, path
from . import views

urlpatterns = [

	path('', views.homepage, name='homepage-view'),
    path('api/ifsc_code=<IFSC>/', views.ifsc_detail, name='ifsc-details'),
    path('api/bank_name=<BANK_NAME>&town=<CITY>/', views.brances_in_city, name='brances-in-city'),
]