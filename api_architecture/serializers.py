from rest_framework import serializers
from .models import *

class BranchSerializer(serializers.ModelSerializer):

	bank = serializers.CharField(source='bank.name')

	class Meta:

		model = Branches
		fields = '__all__'

class SecondaryBranchSerializer(serializers.ModelSerializer):

	class Meta:

		model = Branches
		fields = '__all__'
