from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.tracker, name="TrackingStatus"),
    path("productview/", views.tracker, name="TrackingStatus"),
    path("checkout/", views.tracker, name="TrackingStatus"),

]