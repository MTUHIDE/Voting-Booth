from django.db import models
from enum import IntEnum


# this class is an enumerator to ensure there are only two types of questions, radio and checkbox
class QuestionTypes(IntEnum):
    RADIO = 1
    CHECKBOX = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
# end enumerator


# another enumerator to represent if a question is active or not
class QuestionState(IntEnum):
    INACTIVE = 0;
    ACTIVE = 1;

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
# end enumerator


class Survey(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    type = models.IntegerField(choices=QuestionTypes.choices(), default=QuestionTypes.RADIO)
    state = models.IntegerField(choices=QuestionState.choices(), default=QuestionState.ACTIVE)

    def __str__(self):
        return self.text + ": " + str(self.type)


class Choice(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return ": " + self.text


class Taken(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    student = models.CharField(max_length=20)
