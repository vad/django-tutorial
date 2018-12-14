from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),

    # detail
    path('<int:question_id>/', views.detail, name='question-detail'),
]
