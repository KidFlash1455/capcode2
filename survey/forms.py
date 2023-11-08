from .models import QuestionResponse, QuestionText, QuestionChoice
from django.forms import ModelForm, Select
from django import forms
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404, render


class Survey(ModelForm):
    status = forms.ModelChoiceField(
        label=get_object_or_404(
            QuestionText, question_title__exact="status"
        ).question_text,
        queryset=QuestionChoice.objects.filter(question=5).order_by("-position"),
    )

    class Meta:
        model = QuestionResponse
        fields = [
            "first_name",
            "last_name",
            "suffix",
            "email",
            "status",
        ]
        labels = {
            "first_name": _(
                get_object_or_404(
                    QuestionText, question_title__exact="first name"
                ).question_text
            ),
            "last_name": _(
                get_object_or_404(
                    QuestionText, question_title__exact="last name"
                ).question_text
            ),
            "suffix": _(
                # QuestionText.objects.get(question_title__exact="test").question_text
                get_object_or_404(
                    QuestionText, question_title__exact="suffix"
                ).question_text
            ),
            "email": _(
                get_object_or_404(
                    QuestionText, question_title__exact="email"
                ).question_text
            ),
            # status requires its own custom field
        }
