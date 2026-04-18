from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from .models import Question, Choice, Submission, Lesson


# -----------------------------
# Choice Inline
# -----------------------------
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


# -----------------------------
# Question Inline
# -----------------------------
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# -----------------------------
# Question Admin
# -----------------------------
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('id', 'question_text')


# -----------------------------
# Lesson Admin
# -----------------------------
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Lesson, LessonAdmin)