from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from Projects.views import JoiningRequestsViewSet
from Projects.views import ProjectViewSet
from Projects.views import UsersProjectsViewSet


router: DefaultRouter = DefaultRouter()
router.register("projects", ProjectViewSet, basename="projects")
router.register("users-projects", UsersProjectsViewSet, basename="users-projects")
router.register("joining-requests", JoiningRequestsViewSet, basename="joining-requests")

urlpatterns: list = [
    path("", include(router.urls)),
]
