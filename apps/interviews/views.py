from datetime import datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Interview, Question, QuestionResult
from .serializers import (
    QuestionSerializer,
    InterviewSerializer,
    QuestionResultSerializer
)

class InterviewAPIView(ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
    permission_class = ()

    def get_queryset(self, *args, **kwargs):
        now_date = datetime.now()
        if self.request.user.is_anonymous or (self.request.user and not self.request.user.is_staff):
            return Interview.objects.filter(date_ended__gte=now_date)

        return self.queryset


class QuestionAPIView(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class = ()


class QuestionResultAPIView(ModelViewSet):
    queryset = QuestionResult.objects.all()
    serializer_class = QuestionResultSerializer
    permission_class = ()

    def perform_create(self, serializer):
        user = serializer.validated_data.get('user')
        if not user:
            pass

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return []

        return QuestionResult.objects.filter(user=self.request.user)