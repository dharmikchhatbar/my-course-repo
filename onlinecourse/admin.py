from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class LessonInline(admin.StackedInline):
    """Allows Lessons to be edited inline within CourseAdmin."""
    model = Lesson
    extra = 5

class ChoiceInline(admin.StackedInline):
    """Allows Choices to be edited inline within QuestionAdmin."""
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline):
    """Allows Questions to be edited inline within CourseAdmin."""
    model = Question
    extra = 2

class CourseAdmin(admin.ModelAdmin):
    """Admin configuration for Course model."""
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class QuestionAdmin(admin.ModelAdmin):
    """Admin configuration for Question model."""
    inlines = [ChoiceInline]
    list_display = ['question_text'] 

class LessonAdmin(admin.ModelAdmin):
    """Admin configuration for Lesson model."""
    list_display = ['title']

# Register models with Django admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)