from rest_framework import serializers
from .models import *


class MinistrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Ministry
        fields = '__all__'

class DepartmentSeraizlier(serializers.ModelSerializer):
    ministry = MinistrySerializer()
    class Meta:
        model = Department
        fields = '__all__'

class SchemeSeraizlier(serializers.ModelSerializer):
    ministry  = MinistrySerializer(many = False)
    department  = DepartmentSeraizlier(many = False)
    class Meta:
        model = Scheme
        fields = '__all__'
        
    def to_representation(self, instance):
        # Call the base implementation to get the default representation
        representation = super().to_representation(instance)
        
        # Check if the `ministry` field is None and replace it with an empty string if it is
        if representation['ministry'] is None:
            representation['ministry'] = {'ministry_name': ''}
        elif representation['ministry']['ministry_name'] is None:
            representation['ministry']['ministry_name'] = ''
        
        # Check if the `department` field is None and replace it with an empty string if it is
        if representation['department'] is None:
            representation['department'] = ''
        
        return representation

class BeneficiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Beneficiary
        fields = '__all__'
