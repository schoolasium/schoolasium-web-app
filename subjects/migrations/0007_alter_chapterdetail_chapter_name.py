# Generated by Django 3.2 on 2021-04-06 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0006_auto_20210320_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterdetail',
            name='chapter_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.chapter'),
        ),
    ]