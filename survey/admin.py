from django.contrib import admin
from .models import QuestionResponse, QuestionText, QuestionChoice


class QuestionResponseAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "first_name",
        "last_name",
        "suffix",
        "email",
        "status",
    ]


class QuestionTextAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "question_title",
        "question_text",
    ]


class QuestionChoiceAdmin(admin.ModelAdmin):
    list_display = [
        "question",
        "choice",
        "position",
    ]


admin.site.register(QuestionResponse, QuestionResponseAdmin)
admin.site.register(QuestionText, QuestionTextAdmin)
admin.site.register(QuestionChoice, QuestionChoiceAdmin)
