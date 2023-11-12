from django.db import models


# Create your models here.
class QuestionText(models.Model):
    question_text = models.TextField(max_length=500, default="Default")
    question_title = models.CharField(max_length=200, default="Default")

    def __str__(self):
        return self.question_title


class QuestionResponse(models.Model):
    # Contact Information
    first_name = models.CharField(max_length=100, default="Default")
    last_name = models.CharField(max_length=100, default="Default")
    suffix = models.CharField(max_length=100, default="Default")
    email = models.EmailField(default="Default@default.com")
    status = models.CharField(max_length=500, default="Default")
    status_desc = models.TextField(max_length=500, default="Default")
    # Detailed Information
    university = models.CharField(max_length=100, default="Default")
    university_desc = models.TextField(max_length=500, default="Default")
    department = models.CharField(max_length=100, default="Default")
    university_title = models.CharField(max_length=100, default="Default")
    university_link = models.CharField(max_length=100, default="Default")
    semantic_scholar = models.CharField(max_length=100, default="Default")
    google_scholar = models.CharField(max_length=100, default="Default")
    research_tagline = models.CharField(max_length=300, default="Default")
    research_description = models.CharField(max_length=150, default="Default")
    research_count = models.CharField(max_length=100, default="Default")
    research_example = models.TextField(max_length=500, default="Default")
    data_science_class_1 = models.CharField(max_length=100, default="Default")
    data_science_class_2 = models.CharField(max_length=100, default="Default")
    data_science_class_3 = models.CharField(max_length=100, default="Default")

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name} "


class QuestionChoice(models.Model):
    question = models.ForeignKey(
        "QuestionText",
        related_name="choices",
        on_delete=models.CASCADE,
        default="Default",
    )
    choice = models.TextField(max_length=1000, name="choice", default="default")
    position = models.IntegerField("position")

    def __str__(self):
        return self.choice

    class Meta:
        unique_together = [
            # no duplicated choice per question
            ("question", "choice"),
            # no duplicated position per question
            ("question", "position"),
        ]
        ordering = ("position",)
