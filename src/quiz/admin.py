from django.contrib import admin
import nested_admin
from .models import Category, Quiz, Question, Answer



class Answerinline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 8


class Questioninline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [Answerinline]
    extra = 6
    max_num = 10
    
    
    
    
class QuizAdmin(nested_admin.NestedModelAdmin):
    model = Quiz
    inlines = [Questioninline]



admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)

# Register your models here.
