from django.urls import path
from .views import (
    IndexView,
    DetailView,
    ResultsView,
    # index, detail, results,
    votes
    )

app_name='polls'
urlpatterns = [
    # path('', index, name="index"),
    # path('<int:question_id>/', detail, name="detail"),
    # path('<int:question_id>/results/', results, name="results"),
    path('', IndexView.as_view(), name="index"),
    path('<int:pk>/', DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote/', votes, name="vote"),
]
