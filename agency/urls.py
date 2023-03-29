from django.urls import path

from agency.views import (
    index,
    TopicListView,
    RedactorListView,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("articles/create/", ArticleCreateView.as_view(), name="article-create"),

]

app_name = "agency"
