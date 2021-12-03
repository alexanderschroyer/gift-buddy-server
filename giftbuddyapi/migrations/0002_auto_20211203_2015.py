# Generated by Django 3.2.9 on 2021-12-03 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftbuddyapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='RecipientInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftbuddyapi.interest')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftbuddyapi.recipient')),
            ],
        ),
        migrations.RemoveField(
            model_name='gifter',
            name='profile_image_url',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]