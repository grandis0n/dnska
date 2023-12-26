# Generated by Django 5.0 on 2023-12-25 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'managed': False, 'verbose_name': 'Наличие товара', 'verbose_name_plural': 'Наличие товаров'},
        ),
        migrations.AlterModelOptions(
            name='brands',
            options={'managed': False, 'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'managed': False, 'verbose_name': 'Cart', 'verbose_name_plural': 'Cart'},
        ),
        migrations.AlterModelOptions(
            name='customers',
            options={'managed': False, 'verbose_name': 'Покупатель', 'verbose_name_plural': 'Покупатели'},
        ),
        migrations.AlterModelOptions(
            name='employees',
            options={'managed': False, 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='invoices',
            options={'managed': False, 'verbose_name': 'Счёт-фактура покупателя', 'verbose_name_plural': 'Счёт-фактуры покупателей'},
        ),
        migrations.AlterModelOptions(
            name='orderdetails',
            options={'managed': False, 'verbose_name': 'Детали заказа покупателя', 'verbose_name_plural': 'Детали заказов покупателей'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'managed': False, 'verbose_name': 'Заказ покупателя', 'verbose_name_plural': 'Заказы покупателей'},
        ),
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'managed': False, 'verbose_name': 'Сатус заказа', 'verbose_name_plural': 'Статусы заказов'},
        ),
        migrations.AlterModelOptions(
            name='paymentmethod',
            options={'managed': False, 'verbose_name': 'Метод оплаты', 'verbose_name_plural': 'Методы оплат'},
        ),
        migrations.AlterModelOptions(
            name='paymentstatus',
            options={'managed': False, 'verbose_name': 'Статус оплаты', 'verbose_name_plural': 'Статусы оплат'},
        ),
        migrations.AlterModelOptions(
            name='paymenttype',
            options={'managed': False, 'verbose_name': 'Тип оплаты', 'verbose_name_plural': 'Типы оплаты'},
        ),
        migrations.AlterModelOptions(
            name='permissions',
            options={'managed': False, 'verbose_name': 'Право', 'verbose_name_plural': 'Права'},
        ),
        migrations.AlterModelOptions(
            name='positionpermissions',
            options={'managed': False, 'verbose_name': 'Право должности', 'verbose_name_plural': 'Права должностей'},
        ),
        migrations.AlterModelOptions(
            name='positions',
            options={'managed': False, 'verbose_name': 'Должность', 'verbose_name_plural': 'Должности'},
        ),
        migrations.AlterModelOptions(
            name='productcharacteristicsnew',
            options={'managed': False, 'verbose_name': 'Характеристика товара', 'verbose_name_plural': 'Характеристики товаров'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'managed': False, 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='storeinvoices',
            options={'managed': False, 'verbose_name': 'Счёт-фактура магазина', 'verbose_name_plural': 'Счёт-фактуры магазинов'},
        ),
        migrations.AlterModelOptions(
            name='storeorderdetails',
            options={'managed': False, 'verbose_name': 'Детали заказа магазина', 'verbose_name_plural': 'Детали заказов магазинов'},
        ),
        migrations.AlterModelOptions(
            name='storeorders',
            options={'managed': False, 'verbose_name': 'заказ магазина', 'verbose_name_plural': 'Заказы магазинов'},
        ),
        migrations.AlterModelOptions(
            name='stores',
            options={'managed': False, 'verbose_name': 'магазин', 'verbose_name_plural': 'Магазины'},
        ),
    ]
