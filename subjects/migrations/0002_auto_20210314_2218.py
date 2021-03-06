# Generated by Django 3.1.7 on 2021-03-14 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='activity_link',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='chapter_objective',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='material_link',
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='video_lecture_link',
        ),
        migrations.AlterField(
            model_name='subject',
            name='class_name',
            field=models.CharField(choices=[('All', 'All'), ('Nursury', 'Nursury'), ('Kindergarten', 'Kindergarten'), ('Class-1', 'Class-1'), ('Class-2', 'Class-2'), ('Class-3', 'Class-3'), ('Class-4', 'Class-4'), ('Class-5', 'Class-5'), ('Class-6', 'Class-6'), ('Class-7', 'Class-7'), ('Class-8', 'Class-8'), ('Class-9', 'Class-9'), ('Class-10', 'Class-10')], max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='ChapterDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_objective', models.CharField(max_length=500, null=True)),
                ('material_link', models.CharField(blank=True, max_length=250)),
                ('video_lecture_link', models.CharField(blank=True, max_length=250)),
                ('activity_link', models.CharField(blank=True, max_length=250)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('chapter_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.chapter')),
            ],
        ),
    ]
