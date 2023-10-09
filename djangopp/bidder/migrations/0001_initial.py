# Generated by Django 4.2.5 on 2023-10-09 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('auction_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('reserve_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('auction_status', models.CharField(choices=[('upcoming', 'Upcoming'), ('active', 'Active'), ('ended', 'Ended')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Bidder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('custom_groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_users', to='auth.group')),
                ('custom_user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_users', to='auth.permission')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidder.bidder')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('bid_id', models.AutoField(primary_key=True, serialize=False)),
                ('bid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bid_time', models.DateTimeField()),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidder.auction')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidder.bidder')),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bidder.item'),
        ),
    ]
