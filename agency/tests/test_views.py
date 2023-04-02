from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, Redactor, Article

INDEX_URL = reverse("agency:index")
TOPICS_URL = reverse("agency:topic-list")
TOPICS_SEARCH_URL = reverse("agency:topic-list") + "?name=a"
REDACTORS_URL = reverse("agency:redactor-list")
REDACTORS_SEARCH_URL = reverse("agency:redactor-list") + "?username=a"
ARTICLES_URL = reverse("agency:article-list")
ARTICLES_SEARCH_URL = reverse("agency:article-list") + "?title=a"


class PublicPagesTest(TestCase):
    def test_index_login_required(self):
        res = self.client.get(INDEX_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_manufacturers_login_required(self):
        res = self.client.get(TOPICS_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_drivers_login_required(self):
        res = self.client.get(REDACTORS_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_cars_login_required(self):
        res = self.client.get(ARTICLES_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTest(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="lkjhfdsaW,2",
            first_name="Redactor",
            last_name="Redactorio",
            years_of_experience=7,
        )
        self.client.force_login(self.redactor)

    def test_search_manufacturer_by_name(self):
        Topic.objects.create(name="gooses")
        Topic.objects.create(name="tulips")
        Topic.objects.create(name="lamps")
        res = self.client.get(TOPICS_SEARCH_URL)
        manufacturers = Topic.objects.filter(name__icontains="a")
        self.assertEqual(list(res.context["topic_list"]), list(manufacturers))
        self.assertTemplateUsed(res, "agency/topic_list.html")


class PrivateRedactorTest(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="lkjhfdsaW,2",
            first_name="Redactor",
            last_name="Redactorio",
            years_of_experience=7,
        )
        self.client.force_login(self.redactor)

    def test_search_redactor_by_username(self):
        get_user_model().objects.create(
            username="user_1", password="password", years_of_experience=1
        )
        get_user_model().objects.create(
            username="user_1a", password="password", years_of_experience=2
        )
        get_user_model().objects.create(
            username="user_1b", password="password", years_of_experience=3
        )
        res = self.client.get(REDACTORS_SEARCH_URL)
        drivers = Redactor.objects.filter(username__icontains="a")
        self.assertEqual(list(res.context["redactor_list"]), list(drivers))
        self.assertTemplateUsed(res, "agency/redactor_list.html")


class PrivateActicleTest(TestCase):
    def setUp(self) -> None:
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="lkjhfdsaW,2",
            first_name="Redactor",
            last_name="Redactorio",
            years_of_experience=7,
        )
        self.topic = Topic.objects.create(name="things")
        self.client.force_login(self.redactor)

    def test_car_search_by_model(self):
        Article.objects.create(
            title="The best pizza cutters",
            content="Lorem ipsum dolor sit amet",
            topic=self.topic,
        )
        Article.objects.create(
            title="Must-have bicycle gear",
            content="Lorem ipsum dolor sit amet",
            topic=self.topic,
        )
        Article.objects.create(
            title="Top raincoats for travelers",
            content="Lorem ipsum dolor sit amet",
            topic=self.topic,
        )
        cars = list(Article.objects.filter(title__icontains="a"))
        res = self.client.get(ARTICLES_SEARCH_URL)

        self.assertEqual(
            list(res.context["article_list"]),
            cars,
        )
        self.assertTemplateUsed(res, "agency/article_list.html")
