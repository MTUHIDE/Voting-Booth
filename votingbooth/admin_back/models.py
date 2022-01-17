from django.db import models
from enum import IntEnum


# enumerator to represent if a survey is active or not
class SurveyState(IntEnum):
    INACTIVE = 0
    ACTIVE = 1

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
# end enumerator


# enumerator to represent if a question is active or not
class QuestionState(IntEnum):
    INACTIVE = 0
    ACTIVE = 1

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
# end enumerator


class Survey(models.Model):
    title = models.CharField(max_length=60, unique=True)
    state = models.IntegerField(choices=SurveyState.choices(), default=SurveyState.ACTIVE)

    # def is_active(self):
    #     self.state = 1
    #     return self.state

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    yes = models.IntegerField(default=0)  # Count num of yes votes
    no = models.IntegerField(default=0)  # Count num of no votes
    votes = models.IntegerField(default=0)  # Count num of total votes
    state = models.IntegerField(choices=QuestionState.choices(), default=QuestionState.ACTIVE)

   # def __str__(self):
      #  return self.text + ": " + str(self.type)


class Taken(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    student = models.CharField(max_length=20)
