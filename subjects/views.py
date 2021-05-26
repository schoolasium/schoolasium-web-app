from django.shortcuts import render, redirect
from subjects.models import Subject, Chapter, ChapterDetail
from subjects.forms import CreateChapterForm
from django.contrib.auth.decorators import login_required


def classProfile(request, class_name):
    # print(class_name)
    subject_query = request.GET.get('subject')
    if subject_query:
        subject_query = subject_query.split('/')[0]
    else:
        subject_query = 'Maths'
    # print("subject_query: ", subject_query)

    classes = dict(Subject.CLASSTYPE)

    subjects = Subject.objects.filter(class_name=class_name)
    subject = subjects.filter(subject_name=subject_query).first()

    chapters = Chapter.objects.filter(subject_name=subject)
    chapterDetails = ChapterDetail.objects.filter(subject_name=subject)

    context = {
        "class_name": class_name,
        "classes": classes,
        "subjects": subjects,
        "chapters": chapters,
        "subject": subject,
        "chapterDetails": chapterDetails,
    }
    return render(request, 'subjects/class_page.html', context)


@login_required(login_url='home')
def contents(request):
    if request.method == 'GET':
        classes = dict(Subject.CLASSTYPE)
        classes.pop('All')

        user = request.user
        form = CreateChapterForm()
        context = {
            "form": form,
            "user": user,
            "classes": classes,
        }
        return render(request, 'subjects/contents.html', context)


@login_required(login_url='home')
def classProfileAdmin(request, class_name):
    if request.method == 'GET':
        subject_query = request.GET.get('subject')

        classes = dict(Subject.CLASSTYPE)
        classes.pop('All')

        if request.user != 'AnonymousUser':
            user = request.user

        form = CreateChapterForm(class_name=class_name)

        subjects = Subject.objects.filter(class_name=class_name)

        if subject_query:
            subject_query = subject_query.split('/')[0]
            subject = subjects.filter(subject_name=subject_query).first()
        else:
            subject = None

        chapters = Chapter.objects.filter(subject_name=subject)
        chapterDetails = ChapterDetail.objects.filter(subject_name=subject)

        context = {
            "form": form,
            "user": user,
            "classes": classes,
            "subject": subject,
            "subjects": subjects,
            "class_name": class_name,
            "chapters": chapters,
            "chapterDetails": chapterDetails,
        }
        return render(request, 'subjects/content_class_profile.html', context)
    if request.method == 'POST':
        # Add new chapter
        chapter_name = request.POST['chapter_name']
        post_form = CreateChapterForm(class_name, request.POST)
        # print("post_form: ", post_form)
        if post_form.is_valid():
            # print("form valid")
            subject_name = post_form.cleaned_data['subject_name']
            # print("subject_name: ", type(subject_name))
            # print("subject_name: ", subject_name.id)
            chapterDetailsObj = post_form.save(commit=False)

            chapterObj = Chapter.objects.create(
                subject_name=subject_name,
                chapter_name=chapter_name
            )

            chapterDetailsObj.chapter_name = chapterObj
            chapterDetailsObj.save()
            # print("subject_name: ", subject_name.subject_name)
            # print("subject_name: ", type(subject_name))
            subjectName = subject_name.subject_name

        url = '/content/class/'+class_name+'/?subject='+subjectName

        return redirect(url)


@login_required(login_url='home')
def addSubject(request, class_name):
    if request.method == 'POST':
        post_data = request.POST
        # print("subject_name: ", post_data['subject_name'])
        newSubjectObj = Subject.objects.create(
            class_name=class_name,
            subject_name=post_data['subject_name'],
        )
        print("newSubjectObj: ", newSubjectObj)
        return redirect('class_profile_admin', class_name=class_name)


@login_required(login_url='home')
def addChapterDetails(request, subject_id, chapter_id):
    if request.method == 'POST':
        # print(request.POST)
        subject = Subject.objects.get(id=subject_id)
        chapter = Chapter.objects.get(id=chapter_id)
        newChapterObj = ChapterDetail.objects.create(
            subject_name=subject,
            chapter_name=chapter,
        )
        newChapterObj.chapter_objective = request.POST['chapter_objective_2']
        newChapterObj.material_desc = request.POST['material_desc_2']
        newChapterObj.material_link = request.POST['material_link_2']
        newChapterObj.video_lecture_desc = request.POST['video_lecture_desc_2']
        newChapterObj.video_lecture_link = request.POST['video_lecture_link_2']
        newChapterObj.activity_desc = request.POST['activity_desc_2']
        newChapterObj.activity_link = request.POST['activity_link_2']

        newChapterObj.save()

        class_name = subject.class_name
        subject_name = subject.subject_name

        url = '/content/class/'+class_name+'/?subject='+subject_name

        return redirect(url)
        # return redirect('class_profile_admin', class_name=class_name)
