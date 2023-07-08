from django.urls import path
from . import views


app_name='poll'
urlpatterns = [
    path('',views.IndexView.as_view()),
    path('<int:question_id>/',views.DetailView.as_view(),name='detail'),
    path('<int:question_id>/results/',views.ResultView.as_view(),name='result'),
    path('<int:question_id>/vote/',views.VoteView.as_view(),name='vote')
]
