from django.contrib import admin
from django.urls import path

from questions.views import QuestionView

urlpatterns = [
    path('', QuestionView.as_view()),
    path('admin/', admin.site.urls),
]
