from django.urls import path

from agency.views import (
    index,
    TopicListView,
    RedactorListView,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView, TopicCreateView, TopicUpdateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update", TopicUpdateView.as_view(), name="topic-update"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("articles/create/", ArticleCreateView.as_view(), name="article-create"),
    path("articles/<int:pk>/update", ArticleUpdateView.as_view(), name="article-update"),
    path("articles/<int:pk>/delete", ArticleDeleteView.as_view(), name="article-delete"),

]

app_name = "agency"
