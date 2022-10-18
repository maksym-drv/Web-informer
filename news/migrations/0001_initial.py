# Generated by Django 4.1.2 on 2022-10-18 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('pre_text', models.CharField(max_length=300, null=True, verbose_name='Pre-text')),
                ('full_text', models.TextField(verbose_name='Full-text')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date/time')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Comment text')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Date/time')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news')),
                ('sended_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.users')),
            ],
        ),
    ]