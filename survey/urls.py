from django.urls import path
from .views import SurveyListView, survey, thanks

urlpatterns = [
    path("", SurveyListView.as_view(), name="home"),
    path("survey", survey, name="survey"),
    path("survey/thanks", thanks, name="thanks"),
]
