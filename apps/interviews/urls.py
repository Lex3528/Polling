from django.urls import path

from .views import (
    InterviewAPIView,
    QuestionAPIView,
    QuestionResultAPIView
)

urlpatterns = [
    path(
        'interviews/',
        view=InterviewAPIView.as_view(actions={
            'get': 'list',
            'post': 'create',
        }),
        name='create_order'
    ),
    path(
        'interviews/<int:pk>/',
        view=InterviewAPIView.as_view(actions={
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update',
            'delete': 'delete'
        }),
        name='create_order'
    ),
    path(
        'questions/',
        view=QuestionAPIView.as_view(actions={
            'get': 'list',
            'post': 'create',
        }),
        name='create_order'
    ),
    path(
        'questions/<int:pk>/',
        view=QuestionAPIView.as_view(actions={
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update',
            'delete': 'delete'
        }),
        name='create_order'
    ),
    path(
        'questions/result/',
        view=QuestionResultAPIView.as_view(actions={
            'get': 'list',
            'post': 'create',
        }),
        name='create_order'
    ),
    path(
        'questions/result/<int:pk>/',
        view=QuestionResultAPIView.as_view(actions={
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update',
            'delete': 'delete'
        }),
        name='create_order'
    ),
]