# Generated by Django 4.1.7 on 2023-03-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Success', models.BooleanField(verbose_name='успешность платежа')),
                ('ErrorCode', models.CharField(max_length=250, verbose_name='код ошибки')),
                ('TerminalKey', models.CharField(max_length=250, verbose_name='ключ терминала')),
                ('Status', models.CharField(max_length=250, verbose_name='статус платежа')),
                ('PaymentId', models.CharField(max_length=250, verbose_name='айди платежа')),
                ('OrderId', models.CharField(max_length=250, verbose_name='айди заявки')),
                ('Amount', models.IntegerField(verbose_name='сумма оплаты')),
                ('PaymentURL', models.URLField(verbose_name='ссылка на оплату')),
                ('PaymentDate', models.DateField(auto_now_add=True, verbose_name='дата создания')),
            ],
        ),
    ]
