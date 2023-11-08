from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect, HttpResponse

from .models import QuestionResponse, QuestionText
from .forms import Survey

# Create your views here.


class SurveyListView(ListView):
    model = QuestionText
    template_name = "home.html"


def survey(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Survey(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("survey/thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Survey()

    return render(request, "survey/form.html", {"form": Survey})


def thanks(request):
    return HttpResponse("Thanks!")
