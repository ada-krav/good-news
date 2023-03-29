from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from agency.forms import TopicSearchForm
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

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(TopicListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        contex["search_form"] = TopicSearchForm(
            initial={"name": name}
        )
        return contex

    def get_queryset(self):
        queryset = Topic.objects.all()
        form = TopicSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset

