# Generated by Django 3.0 on 2019-12-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_auto_20191017_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$180000$868mnxxIOGiJ$iiLl531Qb1+Jc+dYrJf7KAAgVyZ3wnBM9vI+n/fPmOA=', max_length=128, verbose_name='password'),
        ),
    ]
