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
        fields = "__all__"
        # "first_name",
        # "last_name",
        # "suffix",
        # "email",
        # "status",
        # "status_desc",
        # "university",
        # "university_desc",
        # "department",
        # "university_title",
        # "university_link",
        # "semantic_scholar",
        # "google_scholar",
        # "research_tagline",

        labels = {
            # Contact Information
            "first_name": _(
                get_object_or_404(
                    QuestionText, question_title__exact="first_name"
                ).question_text
            ),
            "last_name": _(
                get_object_or_404(
                    QuestionText, question_title__exact="last_name"
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
            "status_desc": _(
                get_object_or_404(
                    QuestionText, question_title__exact="status_desc"
                ).question_text
            ),
            # status requires its own custom field
            # Detailed Information
            "university": _(
                get_object_or_404(
                    QuestionText, question_title__exact="university"
                ).question_text
            ),
            "university_desc": _(
                get_object_or_404(
                    QuestionText, question_title__exact="university_desc"
                ).question_text
            ),
            "department": _(
                get_object_or_404(
                    QuestionText, question_title__exact="department"
                ).question_text
            ),
            "university_title": _(
                get_object_or_404(
                    QuestionText, question_title__exact="university_title"
                ).question_text
            ),
            "university_link": _(
                get_object_or_404(
                    QuestionText, question_title__exact="university_link"
                ).question_text
            ),
            "semantic_scholar": _(
                get_object_or_404(
                    QuestionText, question_title__exact="semantic_scholar"
                ).question_text
            ),
            "google_scholar": _(
                get_object_or_404(
                    QuestionText, question_title__exact="google_scholar"
                ).question_text
            ),
            "research_tagline": _(
                get_object_or_404(
                    QuestionText, question_title__exact="research_tagline"
                ).question_text
            ),
            "research_description": _(
                get_object_or_404(
                    QuestionText, question_title__exact="research_description"
                ).question_text
            ),
            "research_count": _(
                get_object_or_404(
                    QuestionText, question_title__exact="research_count"
                ).question_text
            ),
            "research_example": _(
                get_object_or_404(
                    QuestionText, question_title__exact="research_example"
                ).question_text
            ),
            "data_science_class_1": _(
                get_object_or_404(
                    QuestionText, question_title__exact="data_science_class"
                ).question_text
            ),
        }
