# Generated by Django 2.2.6 on 2019-10-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_auto_20191016_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$150000$N2yHsTjBFq4S$tEO+7ykKBF5UMbSbRgk6wmV9Oqj8tKl+3XvZ0ppZAYE=', max_length=128, verbose_name='password'),
        ),
    ]
