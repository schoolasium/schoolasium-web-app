from django.urls import path
from . import views

urlpatterns = [
    path('class/<str:class_name>/', views.classProfile, name="class_profile"),
    path('content/class/<str:class_name>/',
         views.classProfileAdmin, name="class_profile_admin"),
    path('contents/', views.contents, name="content"),
    path('add_content_to_chapter/<int:subject_id>/<int:chapter_id>/',
         views.addChapterDetails, name="add_chapter_details"),
    path('add_subject/<str:class_name>/',
         views.addSubject, name="add_subject"),
]
