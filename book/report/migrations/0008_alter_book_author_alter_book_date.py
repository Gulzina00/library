# Generated by Django 4.0.6 on 2022-08-12 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_book_author_site_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='report.avtor', verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='дата добавление'),
        ),
    ]