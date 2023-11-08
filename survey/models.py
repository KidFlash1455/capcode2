from django.db import models


# Create your models here.
class QuestionText(models.Model):
    question_text = models.TextField(max_length=500, default="Default")
    question_title = models.CharField(max_length=200, default="Default")

    def __str__(self):
        return self.question_title


class QuestionResponse(models.Model):
    first_name = models.CharField(max_length=100, default="Default")
    last_name = models.CharField(max_length=100, default="Default")
    suffix = models.CharField(max_length=100, default="Default")
    email = models.EmailField(default="Default@default.com")
    status = models.CharField(max_length=500, default="Default")


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
