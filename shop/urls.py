from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'availabilities', AvailabilityViewSet)
router.register(r'brands', BrandsViewSet)
router.register(r'carts', CartViewSet)
router.register(r'deliverymethods', DeliverymethodViewSet)
router.register(r'departments', DepartmentsViewSet)
router.register(r'employeepermissions', EmployeepermissionsViewSet)
router.register(r'employeepositions', EmployeepositionsViewSet)
router.register(r'employeesdepartments', EmployeesdepartmentsViewSet)
router.register(r'favouriteproducts', FavouriteproductsViewSet)
router.register(r'invoices', InvoicesViewSet)
router.register(r'orderdetails', OrderdetailsViewSet)
router.register(r'orderstatus', OrderstatusViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'paymentmethods', PaymentmethodViewSet)
router.register(r'paymentstatus', PaymentstatusViewSet)
router.register(r'paymenttypes', PaymenttypeViewSet)
router.register(r'positionpermissions', PositionpermissionsViewSet)
router.register(r'positions', PositionsViewSet)
router.register(r'productcharacteristicsnew', ProductcharacteristicsnewViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'storeinvoices', StoreinvoicesViewSet)
router.register(r'storeorderdetails', StoreorderdetailsViewSet)
router.register(r'storeorders', StoreordersViewSet)
router.register(r'stores', StoresViewSet)
router.register(r'authgroups', AuthGroupViewSet)
router.register(r'authgrouppermissions', AuthGroupPermissionsViewSet)
router.register(r'authpermissions', AuthPermissionViewSet)
router.register(r'authusers', AuthUserViewSet)
router.register(r'authusergroups', AuthUserGroupsViewSet)
router.register(r'authuseruserpermissions', AuthUserUserPermissionsViewSet)
router.register(r'djangoadminlogs', DjangoAdminLogViewSet)
router.register(r'djangocontenttypes', DjangoContentTypeViewSet)
router.register(r'djangomigrations', DjangoMigrationsViewSet)
router.register(r'djangosessions', DjangoSessionViewSet)
router.register(r'employees', EmployeesViewSet)
router.register(r'permissions', PermissionsViewSet)
router.register(r'customers', CustomersViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
