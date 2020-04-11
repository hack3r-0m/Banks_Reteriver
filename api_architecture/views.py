from django.shortcuts import render, HttpResponse
from .models import Banks, Branches
from .serializers import BranchSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def homepage(request):

	return HttpResponse('<h3> Welcome to this BANK RETRIVER API, please read the below instructioins </h3> <br><br> \
						<h3>1)Endpoint for getting bank name from IFSC is /api/ifsc_code=/ <br><br> \
							2)Endpoint for getting all branches in city for desried bank is /api/bank_name=&town=/ <br><br> \
							NOTE : PLEASE USE "%20F" FOR SPACE AND ENTER VALUES IN CAPITAL </h3>')

@api_view(['GET'])
def ifsc_detail(request, IFSC):

	branch = Branches.objects.get(ifsc=IFSC)
	serializer = BranchSerializer(branch)

	return Response(serializer.data)


@api_view(['GET'])
def brances_in_city(request, BANK_NAME, CITY):

	same_city_branches = Branches.objects.filter(bank__name=BANK_NAME, city=CITY)
	serializer = BranchSerializer(same_city_branches, many=True)

	return Response(serializer.data)