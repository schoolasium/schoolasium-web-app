# Generated by Django 3.1.7 on 2021-03-15 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_chapterdetails_subject_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChapterDetails',
            new_name='ChapterDetail',
        ),
    ]
