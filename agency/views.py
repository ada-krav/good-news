from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from agency.forms import (
    TopicSearchForm,
    RedactorSearchForm,
    ArticleSearchForm,
    ArticleForm,
    RedactorCreationForm,
    RedactorUpdateForm,
)
from agency.models import Redactor, Article, Topic


@login_required
def index(request):
    """View function for the home page of the site."""
    num_redactors = Redactor.objects.count()
    num_articles = Article.objects.count()
    num_topics = Topic.objects.count()

    contex = {
        "num_redactors": num_redactors,
        "num_articles": num_articles,
        "num_topics": num_topics,
    }

    return render(request, "agency/index.html", context=contex)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "agency/topic_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        contex["search_form"] = TopicSearchForm(initial={"name": name})
        return contex

    def get_queryset(self):
        queryset = Topic.objects.all()
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    template_name = "agency/redactor_list.html"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        contex["search_form"] = RedactorSearchForm(initial={"username": username})
        return contex

    def get_queryset(self):
        queryset = Redactor.objects.all()
        form = RedactorSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = RedactorUpdateForm
    success_url = reverse_lazy("agency:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("agency:redactor-list")


class ArticleListView(LoginRequiredMixin, generic.ListView):
    model = Article
    paginate_by = 5
    template_name = "agency/article_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(ArticleListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        contex["search_form"] = ArticleSearchForm(initial={"title": title})
        return contex

    def get_queryset(self):
        queryset = Article.objects.all().select_related("topic")
        form = ArticleSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("agency:article-list")


class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy("agency:article-list")


class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Article
    success_url = reverse_lazy("agency:article-list")
