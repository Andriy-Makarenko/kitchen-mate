from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Cook, Dish


class ModelsTests(TestCase):
    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="test_passw123",
            first_name="first_test",
            last_name="second_test",
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})",
        )

    def test_dish_str(self):
        dish_type = (
            DishType.objects.create(name="test")
        )
        dish = (
            Dish.objects.create(
                name="test_name",
                dish_type=dish_type,
                price=20,
            )
        )

        self.assertEqual(str(dish), dish.name)
