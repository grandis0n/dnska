from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from .permissons import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *
from .models import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAuthenticated]


class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
    permission_classes = [IsAuthenticated]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class DeliverymethodViewSet(viewsets.ModelViewSet):
    queryset = Deliverymethod.objects.all()
    serializer_class = DeliverymethodSerializer
    permission_classes = [IsAuthenticated]


class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    permission_classes = [IsAuthenticated]


class EmployeepermissionsViewSet(viewsets.ModelViewSet):
    queryset = Employeepermissions.objects.all()
    serializer_class = EmployeepermissionsSerializer
    permission_classes = [IsAuthenticated]


class EmployeepositionsViewSet(viewsets.ModelViewSet):
    queryset = Employeepositions.objects.all()
    serializer_class = EmployeepositionsSerializer
    permission_classes = [IsAuthenticated]


class EmployeesdepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Employeesdepartments.objects.all()
    serializer_class = EmployeesdepartmentsSerializer
    permission_classes = [IsAuthenticated]


class FavouriteproductsViewSet(viewsets.ModelViewSet):
    queryset = Favouriteproducts.objects.all()
    serializer_class = FavouriteproductsSerializer
    permission_classes = [IsAuthenticated]


class InvoicesViewSet(viewsets.ModelViewSet):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer
    permission_classes = [IsAuthenticated]


class OrderdetailsViewSet(viewsets.ModelViewSet):
    queryset = Orderdetails.objects.all()
    serializer_class = OrderdetailsSerializer
    permission_classes = [IsAuthenticated]


class OrderstatusViewSet(viewsets.ModelViewSet):
    queryset = Orderstatus.objects.all()
    serializer_class = OrderstatusSerializer
    permission_classes = [IsAuthenticated]


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAuthenticated]


class PaymentmethodViewSet(viewsets.ModelViewSet):
    queryset = Paymentmethod.objects.all()
    serializer_class = PaymentmethodSerializer
    permission_classes = [IsAuthenticated]


class PaymentstatusViewSet(viewsets.ModelViewSet):
    queryset = Paymentstatus.objects.all()
    serializer_class = PaymentstatusSerializer
    permission_classes = [IsAuthenticated]


class PaymenttypeViewSet(viewsets.ModelViewSet):
    queryset = Paymenttype.objects.all()
    serializer_class = PaymenttypeSerializer
    permission_classes = [IsAuthenticated]


class PositionpermissionsViewSet(viewsets.ModelViewSet):
    queryset = Positionpermissions.objects.all()
    serializer_class = PositionpermissionsSerializer
    permission_classes = [IsAuthenticated]


class PositionsViewSet(viewsets.ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = [IsAuthenticated]


class ProductcharacteristicsnewViewSet(viewsets.ModelViewSet):
    queryset = Productcharacteristicsnew.objects.all()
    serializer_class = ProductcharacteristicsnewSerializer
    permission_classes = [IsAuthenticated]


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAuthenticated]


class StoreinvoicesViewSet(viewsets.ModelViewSet):
    queryset = Storeinvoices.objects.all()
    serializer_class = StoreinvoicesSerializer
    permission_classes = [IsAuthenticated]


class StoreorderdetailsViewSet(viewsets.ModelViewSet):
    queryset = Storeorderdetails.objects.all()
    serializer_class = StoreorderdetailsSerializer
    permission_classes = [IsAuthenticated]


class StoreordersViewSet(viewsets.ModelViewSet):
    queryset = Storeorders.objects.all()
    serializer_class = StoreordersSerializer
    permission_classes = [IsAuthenticated]


class StoresViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer
    permission_classes = [IsAuthenticated]


class AuthGroupViewSet(viewsets.ModelViewSet):
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer
    permission_classes = [IsAuthenticated]


class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthGroupPermissions.objects.all()
    serializer_class = AuthGroupPermissionsSerializer
    permission_classes = [IsAuthenticated]


class AuthPermissionViewSet(viewsets.ModelViewSet):
    queryset = AuthPermission.objects.all()
    serializer_class = AuthPermissionSerializer
    permission_classes = [IsAuthenticated]


class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer
    permission_classes = [IsAuthenticated]


class AuthUserGroupsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserGroups.objects.all()
    serializer_class = AuthUserGroupsSerializer
    permission_classes = [IsAuthenticated]


class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserUserPermissions.objects.all()
    serializer_class = AuthUserUserPermissionsSerializer
    permission_classes = [IsAuthenticated]


class DjangoAdminLogViewSet(viewsets.ModelViewSet):
    queryset = DjangoAdminLog.objects.all()
    serializer_class = DjangoAdminLogSerializer
    permission_classes = [IsAuthenticated]


class DjangoContentTypeViewSet(viewsets.ModelViewSet):
    queryset = DjangoContentType.objects.all()
    serializer_class = DjangoContentTypeSerializer
    permission_classes = [IsAuthenticated]


class DjangoMigrationsViewSet(viewsets.ModelViewSet):
    queryset = DjangoMigrations.objects.all()
    serializer_class = DjangoMigrationsSerializer
    permission_classes = [IsAuthenticated]


class DjangoSessionViewSet(viewsets.ModelViewSet):
    queryset = DjangoSession.objects.all()
    serializer_class = DjangoSessionSerializer
    permission_classes = [IsAuthenticated]


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated]


class PermissionsViewSet(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    permission_classes = [IsAuthenticated]


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = [IsAuthenticated]
