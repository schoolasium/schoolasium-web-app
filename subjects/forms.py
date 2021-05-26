from django.forms import ModelForm
from subjects.models import ChapterDetail, Subject


class CreateChapterForm(ModelForm):
    class Meta:
        model = ChapterDetail
        fields = '__all__'
        exclude = ['is_deleted', 'date_created',
                   'date_updated', 'chapter_name']

    # Only client belonging to agency will appear
    def __init__(self, class_name=None, *args, ** kwargs):
        super(CreateChapterForm, self).__init__(*args, **kwargs)
        if class_name:
            self.fields['subject_name'].queryset = Subject.objects.filter(
                class_name=class_name, is_deleted=False)


class CreateSubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        exclude = ['is_deleted', 'date_created', 'date_updated']
