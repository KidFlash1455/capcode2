from django.contrib import admin
from .models import QuestionResponse, QuestionText, QuestionChoice


class QuestionResponseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in QuestionResponse._meta.get_fields()]


class QuestionTextAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "question_title",
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
