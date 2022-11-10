from django.urls import path

from .views import (
    index,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    DriverListView,
    DriverDetailView,
    DriverCreateView,
    DriverLicenseUpdateView,
    DriverDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    toggle_assign_to_car,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish_types/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish_types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),


app_name = "restaurant"