from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact_us", views.contact_us, name="contact_us"),
    path("project/<int:project_id>", views.project, name="project"),
    path("about_me", views.about_me, name="about_me"),
]
