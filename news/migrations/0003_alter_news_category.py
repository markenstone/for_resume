# Generated by Django 4.0.5 on 2022-07-11 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_category_alter_news_options_alter_news_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='категория'),
        ),
    ]