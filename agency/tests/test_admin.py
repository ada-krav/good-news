from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="asdfhjkl",
            first_name="Admin",
            last_name="Admineo",
            years_of_experience=77,
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="redactor",
            password="lkjhfdsaW,2",
            first_name="Redactor",
            last_name="Redactorio",
            years_of_experience=7,
        )

    def test_driver_license_number_listed(self):
        url = reverse("admin:agency_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_experience)
