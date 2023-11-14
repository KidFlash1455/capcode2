from .models import QuestionResponse, QuestionText, QuestionChoice
from django.forms import ModelForm, Select
from django import forms
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404, render


class Survey(ModelForm):
    status = forms.ModelChoiceField(
        queryset=QuestionChoice.objects.filter(question=1).order_by("-position"),
    )

    class Meta:
        model = QuestionResponse
        fields = "__all__"
