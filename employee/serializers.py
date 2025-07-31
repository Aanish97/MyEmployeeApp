from rest_framework import serializers
from .models import Employee, Address, AddressType


class AddressTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressType
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    address_type = AddressTypeSerializer()

    class Meta:
        model = Address
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
