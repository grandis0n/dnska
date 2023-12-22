from django.db import models


class Availability(models.Model):
    id = models.AutoField(primary_key=True)
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductID', blank=True,
                                  null=True, verbose_name='Наименование')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True, verbose_name='Количество:')  # Field name made lowercase.
    storeid = models.ForeignKey('Stores', models.DO_NOTHING, db_column='StoreID', blank=True, verbose_name='Магазин:',
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Availability'
        verbose_name = 'Наличие товара'
        verbose_name_plural = 'Наличие товаров'

    def __str__(self):
        return f"{self.productid.name} Колличество: {self.quantity} Магазин: {self.storeid.city} {self.storeid.street} {self.storeid.building}"

class Brands(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.TextField(db_column='Name', verbose_name = 'Название')  # Field name made lowercase.
    country = models.TextField(db_column='Country', verbose_name = 'Страна', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Brands'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    userid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'


class Categories(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categories'


# Unable to inspect table 'Customers'
# The error was: list index out of range


class Deliverymethod(models.Model):
    deliveryid = models.AutoField(db_column='DeliveryID', primary_key=True, blank=True,
                                  null=False)  # Field name made lowercase.
    deliverytype = models.TextField(db_column='DeliveryType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeliveryMethod'


class Departments(models.Model):
    departmentid = models.AutoField(db_column='DepartmentID', primary_key=True, blank=True,
                                    null=False)  # Field name made lowercase.
    departmentname = models.TextField(db_column='DepartmentName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departments'


class Employeepermissions(models.Model):
    employeepermissionid = models.AutoField(db_column='EmployeePermissionID', primary_key=True, blank=True,
                                            null=False)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='EmployeeID', blank=True,
                                   null=False)  # Field name made lowercase.
    permissionid = models.ForeignKey('Permissions', models.DO_NOTHING, db_column='PermissionID', blank=True,
                                     null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeePermissions'


class Employeepositions(models.Model):
    employeepositionid = models.AutoField(db_column='EmployeePositionID', primary_key=True, blank=True,
                                          null=False)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='EmployeeID', blank=True,
                                   null=False)  # Field name made lowercase.
    positionid = models.ForeignKey('Positions', models.DO_NOTHING, db_column='PositionID', blank=True,
                                   null=False)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    dateassigned = models.DateField(db_column='DateAssigned', blank=True, null=True)  # Field name made lowercase.
    dateremoved = models.DateField(db_column='DateRemoved', blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeePositions'

class Employeesdepartments(models.Model):
    employeeid = models.OneToOneField('Employees', models.DO_NOTHING, db_column='EmployeeID', primary_key=True,
                                      blank=True,
                                      null=False)  # Field name made lowercase. The composite primary key (EmployeeID, DepartmentID) found, that is not supported. The first column is selected.
    departmentid = models.ForeignKey(Departments, models.DO_NOTHING, db_column='DepartmentID', blank=True,
                                     null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmployeesDepartments'


class Favouriteproducts(models.Model):
    userid = models.OneToOneField('Customers', models.DO_NOTHING, db_column='UserID', primary_key=True, blank=True,
                                  null=False)  # Field name made lowercase. The composite primary key (UserID, ProductID) found, that is not supported. The first column is selected.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductID', blank=True,
                                  null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FavouriteProducts'


class Invoices(models.Model):
    invoiceid = models.AutoField(db_column='InvoiceID', primary_key=True, blank=True,
                                 null=False)  # Field name made lowercase.
    orderid = models.OneToOneField('Orders', models.DO_NOTHING, db_column='OrderID', verbose_name = 'Заказ')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', verbose_name = 'Сумма оплаты')  # Field name made lowercase.
    paymentstatusid = models.ForeignKey('Paymentstatus', models.DO_NOTHING,
                                        db_column='PaymentStatusID', verbose_name = 'Статус оплаты')  # Field name made lowercase.
    paymenttypeid = models.ForeignKey('Paymenttype', models.DO_NOTHING,
                                      db_column='PaymentTypeID', verbose_name = 'Тип оплаты')  # Field name made lowercase.
    paymentmethodid = models.ForeignKey('Paymentmethod', models.DO_NOTHING,
                                        db_column='PaymentMethodID', verbose_name = 'Метод оплаты')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Invoices'
        verbose_name = 'Счёт-фактура покупателя'
        verbose_name_plural = 'Счёт-фактуры покупателей'

    def __str__(self):
        return f"<{self.orderid.orderid}> {self.amount} рублей"


class Orderdetails(models.Model):
    orderdetailid = models.AutoField(db_column='OrderDetailID', primary_key=True, blank=True,
                                     null=False)  # Field name made lowercase.
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderID', verbose_name = 'Заказ')  # Field name made lowercase.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductID', verbose_name = 'Товар')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', verbose_name = 'Количество')  # Field name made lowercase.
    price = models.FloatField(db_column='Price', verbose_name = 'Цена')  # Field name made lowercase.
    statusid = models.ForeignKey('Orderstatus', models.DO_NOTHING, db_column='StatusID', verbose_name = 'Cтатус заказа')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderDetails'
        verbose_name = 'Детали заказа покупателя'
        verbose_name_plural = 'Детали заказов покупателей'

    def __str__(self):
        return f"<{self.orderid.orderid}> {self.productid} | {self.quantity} шт. | {self.price} рублей | {self.statusid} |"


class Orderstatus(models.Model):
    statusid = models.AutoField(db_column='StatusID', primary_key=True, blank=True,
                                null=False)  # Field name made lowercase.
    statusname = models.TextField(db_column='StatusName', verbose_name = 'Название')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderStatus'
        verbose_name = 'Сатус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return f"{self.statusname}"


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True, blank=True,
                               null=False)  # Field name made lowercase.
    userid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='UserID', verbose_name = 'Покупатель', blank=True,
                               null=False)  # Field name made lowercase.
    date = models.DateField(db_column='Date', verbose_name = 'Дата заказа')  # Field name made lowercase.
    statusid = models.ForeignKey(Orderstatus, models.DO_NOTHING, db_column='StatusID', verbose_name = 'Статус заказа')  # Field name made lowercase.
    deliveryid = models.ForeignKey(Deliverymethod, models.DO_NOTHING,
                                   db_column='DeliveryID', verbose_name = 'Метод доставки')  # Field name made lowercase.
    storeid = models.ForeignKey('Stores', models.DO_NOTHING, db_column='StoreID', verbose_name = 'Магазин')  # Field name made lowercase.
    invoiceid = models.ForeignKey(Invoices, models.DO_NOTHING, db_column='InvoiceID', blank=True,
                                  null=True, verbose_name = 'Счёт-фактура')  # Field name made lowercase.
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True, verbose_name = 'Ответственный сотрудник')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'
        verbose_name = 'Заказ покупателя'
        verbose_name_plural = 'Заказы покупателей'

    def __str__(self):
        return f"<{self.orderid}> | {self.userid} | {self.storeid} | {self.invoiceid.amount} рублей | {self.statusid} | {self.invoiceid.paymentstatusid} | {self.employeeid} |"


class Paymentmethod(models.Model):
    paymentmethodid = models.AutoField(db_column='PaymentMethodID', primary_key=True, blank=True,
                                       null=False)  # Field name made lowercase.
    methodname = models.TextField(db_column='MethodName', verbose_name = 'Наименование')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentMethod'
        verbose_name = 'Метод оплаты'
        verbose_name_plural = 'Методы оплат'

    def __str__(self):
        return f"{self.methodname}"


class Paymentstatus(models.Model):
    paymentstatusid = models.AutoField(db_column='PaymentStatusID', primary_key=True, blank=True,
                                       null=False)  # Field name made lowercase.
    statusname = models.TextField(db_column='StatusName', verbose_name = 'Наименование')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentStatus'
        verbose_name = 'Статус оплаты'
        verbose_name_plural = 'Статусы оплат'

    def __str__(self):
        return f"{self.statusname}"


class Paymenttype(models.Model):
    paymenttypeid = models.AutoField(db_column='PaymentTypeID', primary_key=True, blank=True,
                                     null=False)  # Field name made lowercase.
    typename = models.TextField(db_column='TypeName', verbose_name = 'Наименование')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentType'
        verbose_name = 'Тип оплаты'
        verbose_name_plural = 'Типы оплаты'

    def __str__(self):
        return f"{self.typename}"


class Positionpermissions(models.Model):
    positionpermissionid = models.AutoField(db_column='PositionPermissionID', primary_key=True, blank=True,
                                            null=False)  # Field name made lowercase.
    positionid = models.ForeignKey('Positions', models.DO_NOTHING, db_column='PositionID', verbose_name = 'Должность', blank=True,
                                   null=False)  # Field name made lowercase.
    permissionid = models.ForeignKey('Permissions', models.DO_NOTHING, db_column='PermissionID', verbose_name = 'Право', blank=True,
                                     null=False)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PositionPermissions'
        verbose_name = 'Право должности'
        verbose_name_plural = 'Права должностей'

    def __str__(self):
        return f"{self.positionid}"


class Positions(models.Model):
    positionid = models.AutoField(db_column='PositionID', primary_key=True, blank=True,
                                  null=False)  # Field name made lowercase.
    positionname = models.TextField(db_column='PositionName', blank=True, null=True, verbose_name = 'Должность')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True, verbose_name = 'Описание должности')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Positions'
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return f"{self.positionname}"



class Productcharacteristicsnew(models.Model):
    productcharacteristicid = models.AutoField(db_column='ProductCharacteristicID', primary_key=True, blank=True,
                                               null=False)  # Field name made lowercase.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductID', verbose_name = 'Товар')  # Field name made lowercase.
    characteristics = models.TextField(db_column='Characteristics', verbose_name = 'Характеристики', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductCharacteristicsNew'
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товаров'

    def __str__(self):
        return f"{self.productid} - {self.characteristics}"


class Products(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    sku = models.TextField(db_column='SKU', unique=True, verbose_name = 'Штрихкод')  # Field name made lowercase.
    name = models.TextField(db_column='Name', verbose_name = 'Наименование')  # Field name made lowercase.
    description = models.TextField(db_column='Description', verbose_name = 'Описание', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, verbose_name = 'Цена', null=True)  # Field name made lowercase.
    brandid = models.ForeignKey(Brands, models.DO_NOTHING, db_column='BrandID', verbose_name = 'Бренд', blank=True,
                                null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoryID', verbose_name = 'Категория', blank=True,
                                   null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.name} "


class Storeinvoices(models.Model):
    invoiceid = models.AutoField(db_column='InvoiceID', primary_key=True, blank=True,
                                 null=False)  # Field name made lowercase.
    storeorderid = models.OneToOneField('Storeorders', models.DO_NOTHING,
                                        db_column='StoreOrderID', verbose_name = 'Магазин')  # Field name made lowercase.
    sum = models.IntegerField(db_column='Sum', verbose_name = 'Сумма платежа')  # Field name made lowercase.
    invoicedate = models.DateField(db_column='InvoiceDate', verbose_name = 'Дата платежа')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoreInvoices'
        verbose_name = 'Счёт-фактура магазина'
        verbose_name_plural = 'Счёт-фактуры магазинов'

    def __str__(self):
        return f"{self.storeorderid} {self.sum} рублей //{self.invoicedate}//"


class Storeorderdetails(models.Model):
    storeorderdetailid = models.AutoField(db_column='StoreOrderDetailID', primary_key=True, blank=True,
                                          null=False)  # Field name made lowercase.
    storeorderid = models.ForeignKey('Storeorders', models.DO_NOTHING,
                                     db_column='StoreOrderID', verbose_name = 'Номер заказа')  # Field name made lowercase.
    productid = models.ForeignKey(Products, models.DO_NOTHING, db_column='ProductID', verbose_name = 'Товар')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', verbose_name = 'Количество')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoreOrderDetails'
        verbose_name = 'Детали заказа магазина'
        verbose_name_plural = 'Детали заказов магазинов'

    def __str__(self):
        return f"{self.storeorderid} {self.productid} Количество: {self.quantity} шт. //{self.storeorderid.orderdate}//"


class Storeorders(models.Model):
    storeorderid = models.AutoField(db_column='StoreOrderID', primary_key=True, blank=True,
                                    null=False)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employees', models.DO_NOTHING, db_column='EmployeeID', verbose_name = 'Сотрудник', blank=True,
                                   null=False)  # Field name made lowercase.
    storeid = models.ForeignKey('Stores', models.DO_NOTHING, db_column='StoreID', verbose_name = 'Магазин')  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', verbose_name = 'Дата заказа')  # Field name made lowercase.
    status = models.TextField(db_column='Status', verbose_name = 'Статус заказа')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoreOrders'
        verbose_name = 'заказ магазина'
        verbose_name_plural = 'Заказы магазинов'

    def __str__(self):
        return f"<{self.storeorderid}>"



class Stores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    city = models.TextField(db_column='City', verbose_name = 'Город', blank=True, null=True)  # Field name made lowercase.
    street = models.TextField(db_column='Street', verbose_name = 'Улица', blank=True, null=True)  # Field name made lowercase.
    building = models.TextField(db_column='Building', verbose_name = 'Строение', blank=True, null=True)  # Field name made lowercase.
    area = models.TextField(db_column='Area', verbose_name = 'Район', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stores'
        verbose_name = 'магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return f"г. {self.city}, ул. {self.street}, д. {self.building}, {self.area} район"




class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    FirstName = models.TextField(verbose_name = 'Имя')
    LastName = models.TextField(verbose_name = 'Фамилия')
    Email = models.EmailField(max_length=319, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=12, verbose_name = 'Номер телефона')
    HireDate = models.DateField(null=True, blank=True, verbose_name = 'Дата зачисления')
    Salary = models.FloatField(null=True, blank=True, verbose_name = 'Зарплата')
    Status = models.CharField(max_length=10, choices=[('Активен', 'Активен'), ('Уволен', 'Уволен')], default='Активен', verbose_name = 'Статус')
    DismissalDate = models.DateField(null=True, blank=True, verbose_name = 'Дата увольнения')


    class Meta:
        managed = False
        db_table = 'Employees'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.LastName} {self.FirstName}"



class Permissions(models.Model):
    PermissionID = models.AutoField(primary_key=True)
    PermissionName = models.TextField(verbose_name = 'Название')
    Description = models.TextField(null=True, blank=True, verbose_name = 'Описание')

    class Meta:
        managed = False
        db_table = 'Permissions'
        verbose_name = 'Право'
        verbose_name_plural = 'Права'

    def __str__(self):
        return f"<{self.PermissionID}> {self.PermissionName}"


class Customers(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.TextField()
    Email = models.EmailField(max_length=319, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=12, unique=True)
    Address = models.TextField(null=True, blank=True)


    class Meta:
        managed = False
        db_table = 'Customers'
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f"{self.Name} | {self.PhoneNumber}"
