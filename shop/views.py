from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from .permissons import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *
from .models import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    permission_classes = [IsAdminOrReadOnly]


class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
    permission_classes = [IsAdminOrReadOnly]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminOrReadOnly, IsOwnerOrReadOnly]


class DeliverymethodViewSet(viewsets.ModelViewSet):
    queryset = Deliverymethod.objects.all()
    serializer_class = DeliverymethodSerializer
    permission_classes = [IsAdminOrReadOnly]


class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    permission_classes = [IsAdminUser]


class EmployeepermissionsViewSet(viewsets.ModelViewSet):
    queryset = Employeepermissions.objects.all()
    serializer_class = EmployeepermissionsSerializer
    permission_classes = [IsAdminUser]


class EmployeepositionsViewSet(viewsets.ModelViewSet):
    queryset = Employeepositions.objects.all()
    serializer_class = EmployeepositionsSerializer
    permission_classes = [IsAdminUser]


class EmployeesdepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Employeesdepartments.objects.all()
    serializer_class = EmployeesdepartmentsSerializer
    permission_classes = [IsAdminUser]


class FavouriteproductsViewSet(viewsets.ModelViewSet):
    queryset = Favouriteproducts.objects.all()
    serializer_class = FavouriteproductsSerializer
    permission_classes = [IsAdminOrReadOnly]


class InvoicesViewSet(viewsets.ModelViewSet):
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer
    permission_classes = [IsAdminUser]


class OrderdetailsViewSet(viewsets.ModelViewSet):
    queryset = Orderdetails.objects.all()
    serializer_class = OrderdetailsSerializer
    permission_classes = [IsAdminOrReadOnly]


class OrderstatusViewSet(viewsets.ModelViewSet):
    queryset = Orderstatus.objects.all()
    serializer_class = OrderstatusSerializer
    permission_classes = [IsAdminOrReadOnly]


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [IsAdminOrReadOnly]


class PaymentmethodViewSet(viewsets.ModelViewSet):
    queryset = Paymentmethod.objects.all()
    serializer_class = PaymentmethodSerializer
    permission_classes = [IsAdminOrReadOnly]


class PaymentstatusViewSet(viewsets.ModelViewSet):
    queryset = Paymentstatus.objects.all()
    serializer_class = PaymentstatusSerializer
    permission_classes = [IsAdminOrReadOnly]


class PaymenttypeViewSet(viewsets.ModelViewSet):
    queryset = Paymenttype.objects.all()
    serializer_class = PaymenttypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class PositionpermissionsViewSet(viewsets.ModelViewSet):
    queryset = Positionpermissions.objects.all()
    serializer_class = PositionpermissionsSerializer
    permission_classes = [IsAdminUser]


class PositionsViewSet(viewsets.ModelViewSet):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = [IsAdminUser]


class ProductcharacteristicsnewViewSet(viewsets.ModelViewSet):
    queryset = Productcharacteristicsnew.objects.all()
    serializer_class = ProductcharacteristicsnewSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsAdminOrReadOnly]


class StoreinvoicesViewSet(viewsets.ModelViewSet):
    queryset = Storeinvoices.objects.all()
    serializer_class = StoreinvoicesSerializer
    permission_classes = [IsAdminUser]


class StoreorderdetailsViewSet(viewsets.ModelViewSet):
    queryset = Storeorderdetails.objects.all()
    serializer_class = StoreorderdetailsSerializer
    permission_classes = [IsAdminUser]


class StoreordersViewSet(viewsets.ModelViewSet):
    queryset = Storeorders.objects.all()
    serializer_class = StoreordersSerializer
    permission_classes = [IsAdminUser]


class StoresViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer
    permission_classes = [IsAdminOrReadOnly]


class AuthGroupViewSet(viewsets.ModelViewSet):
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer
    # permission_classes = [IsAdminUser]


class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthGroupPermissions.objects.all()
    serializer_class = AuthGroupPermissionsSerializer
    # permission_classes = [IsAdminUser]


class AuthPermissionViewSet(viewsets.ModelViewSet):
    queryset = AuthPermission.objects.all()
    serializer_class = AuthPermissionSerializer
    # permission_classes = [IsAdminUser]


class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer
    # permission_classes = [IsAdminUser]


class AuthUserGroupsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserGroups.objects.all()
    serializer_class = AuthUserGroupsSerializer
    # permission_classes = [IsAdminUser]


class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserUserPermissions.objects.all()
    serializer_class = AuthUserUserPermissionsSerializer
    # permission_classes = [IsAdminUser]


class DjangoAdminLogViewSet(viewsets.ModelViewSet):
    queryset = DjangoAdminLog.objects.all()
    serializer_class = DjangoAdminLogSerializer
    permission_classes = [IsAdminUser]


class DjangoContentTypeViewSet(viewsets.ModelViewSet):
    queryset = DjangoContentType.objects.all()
    serializer_class = DjangoContentTypeSerializer
    permission_classes = [IsAdminUser]


class DjangoMigrationsViewSet(viewsets.ModelViewSet):
    queryset = DjangoMigrations.objects.all()
    serializer_class = DjangoMigrationsSerializer
    permission_classes = [IsAdminUser]


class DjangoSessionViewSet(viewsets.ModelViewSet):
    queryset = DjangoSession.objects.all()
    serializer_class = DjangoSessionSerializer
    # permission_classes = [IsAdminUser]


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAdminUser]


class PermissionsViewSet(viewsets.ModelViewSet):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    permission_classes = [IsAdminUser]


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = [IsAdminUser]
