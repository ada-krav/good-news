from django.urls import path

from agency.views import (
    index,
    TopicListView,
    RedactorListView,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    RedactorDetailView,
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    articles_by_topic,
)


urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete", TopicDeleteView.as_view(), name="topic-delete"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/create", RedactorCreateView.as_view(), name="redactor-create"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path(
        "redactors/<int:pk>/update",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
    path(
        "redactors/<int:pk>/delete",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("articles/create/", ArticleCreateView.as_view(), name="article-create"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path(
        "articles/<int:pk>/update", ArticleUpdateView.as_view(), name="article-update"
    ),
    path(
        "articles/<int:pk>/delete", ArticleDeleteView.as_view(), name="article-delete"
    ),
    path("articles/about/<str:topic>", articles_by_topic, name="article-topic"),
]

app_name = "agency"
