from django.db import models


class Subject(models.Model):
    CLASSTYPE = (
        ('All', 'All'),
        ('Nursury', 'Nursury'),
        ('Kindergarten', 'Kindergarten'),
        ('Class-1', 'Class-1'),
        ('Class-2', 'Class-2'),
        ('Class-3', 'Class-3'),
        ('Class-4', 'Class-4'),
        ('Class-5', 'Class-5'),
        ('Class-6', 'Class-6'),
        ('Class-7', 'Class-7'),
        ('Class-8', 'Class-8'),
        ('Class-9', 'Class-9'),
        ('Class-10', 'Class-10'),
    )
    class_name = models.CharField(
        max_length=250, null=True, choices=CLASSTYPE)
    subject_name = models.CharField(max_length=250, null=True)

    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.class_name + '-' + self.subject_name


class Chapter(models.Model):
    subject_name = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True)
    chapter_name = models.CharField(max_length=250, null=True)

    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.subject_name.class_name + '-' + self.subject_name.subject_name + '-' + self.chapter_name


class ChapterDetail(models.Model):
    subject_name = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True)
    chapter_name = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, null=True)
    chapter_objective = models.CharField(max_length=500, null=True)
    material_desc = models.CharField(max_length=250, blank=True)
    material_link = models.CharField(max_length=250, blank=True)
    video_lecture_desc = models.CharField(max_length=250, blank=True)
    video_lecture_link = models.CharField(max_length=250, blank=True)
    activity_desc = models.CharField(max_length=250, blank=True)
    activity_link = models.CharField(max_length=250, blank=True)

    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.chapter_name.chapter_name+'-'+str(self.id)
