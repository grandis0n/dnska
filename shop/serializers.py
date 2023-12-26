from requests import Response
from rest_framework import serializers, status
from rest_framework.views import APIView

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class DeliverymethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliverymethod
        fields = '__all__'


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'


class EmployeepermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeepermissions
        fields = '__all__'


class EmployeepositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeepositions
        fields = '__all__'


class EmployeesdepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employeesdepartments
        fields = '__all__'


class FavouriteproductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favouriteproducts
        fields = "__all__"


class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = '__all__'


class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetails
        fields = '__all__'


class OrderstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderstatus
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrderstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderstatus
        fields = '__all__'


class OrderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderdetails
        fields = '__all__'


class PaymentmethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paymentmethod
        fields = '__all__'


class PaymentstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paymentstatus
        fields = '__all__'


class PaymenttypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paymenttype
        fields = '__all__'


class PositionpermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positionpermissions
        fields = '__all__'


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'


class ProductcharacteristicsnewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productcharacteristicsnew
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class StoreinvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storeinvoices
        fields = '__all__'


class StoreorderdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storeorderdetails
        fields = '__all__'


class StoreordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storeorders
        fields = '__all__'


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = '__all__'


class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = '__all__'


class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'


class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = '__all__'


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'


class AuthUserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = '__all__'


class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'


class DjangoAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = '__all__'


class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = '__all__'


class DjangoMigrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = '__all__'


class DjangoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoSession
        fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
