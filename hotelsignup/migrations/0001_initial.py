# Generated by Django 4.0.2 on 2022-04-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotelsignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_name', models.CharField(max_length=255)),
                ('hotel_name', models.CharField(max_length=255)),
                ('hotel_phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('hotel_email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('ZONE', models.CharField(max_length=255)),
                ('CAPACITY', models.CharField(max_length=255)),
                ('hotel_image_upload', models.ImageField(blank=True, null=True, upload_to='static/images/hotelsignupimages/PROFILE_PICS')),
                ('auth_doc_upload', models.ImageField(blank=True, null=True, upload_to='static/images/hotelsignupimages/AUTHENTICATION_DOCS')),
                ('author', models.BooleanField()),
            ],
        ),
    ]
