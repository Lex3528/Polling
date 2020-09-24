from rest_framework import serializers

from .models import Interview, Question, QuestionResult


class InterviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interview
        fields = (
            'name',
            'date_started',
            'date_ended',
            'description'
        )


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'text',
            'type',
            'users'
        )


class QuestionResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionResult
        fields = (
            'user',
            'question',
            'result'
        )