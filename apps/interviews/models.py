from django.db import models


class Interview(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    date_started = models.DateTimeField(auto_now_add=True)
    date_ended = models.DateTimeField(null=True, blank=True)
    description = models.TextField()


class Question(models.Model):
    TEXT_TYPE = 'text_type'
    ONE_CHOICE_TYPE = 'one_choice_type'
    MANY_CHOICE_TYPE = 'many_choice_type'

    QUESTION_TYPE_CHOICES = (
        (TEXT_TYPE, 'Текстовый'),
        (ONE_CHOICE_TYPE, 'Один вариант'),
        (MANY_CHOICE_TYPE, 'Много вариантов')
    )

    text = models.CharField(max_length=255)
    type = models.CharField(choices=QUESTION_TYPE_CHOICES, default=TEXT_TYPE, max_length=20)
    users = models.ManyToManyField('users.User', through='QuestionResult')


class QuestionResult(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    result = models.CharField(max_length=255)
