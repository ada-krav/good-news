from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from agency.models import Article, Redactor


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=63,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class ArticleSearchForm(forms.Form):
    title = forms.CharField(
        max_length=127,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title"}
        )
    )


class ArticleForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Article
        fields = "__all__"


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = [
            "years_of_experience",
            "first_name",
            "last_name"
        ]
