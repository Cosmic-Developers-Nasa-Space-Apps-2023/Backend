from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from Projects.models import Project, UsersProjects, JoiningRequests
from Projects.serializers import ProjectSerializer, UsersProjectsSerializer, JoiningRequestsSerializer
from Users.permissions import IsAdmin
from Users.permissions import IsVerified


class ProjectViewSet(ModelViewSet):
    queryset: QuerySet = Project.objects.all().order_by("-id")
    lookup_url_kwarg: str = "pk"
    serializer_class: ProjectSerializer = ProjectSerializer
    permission_classes: list = [IsAuthenticated & IsVerified & IsAdmin]


class UsersProjectsViewSet(ModelViewSet):
    queryset: QuerySet = UsersProjects.objects.all().order_by("-id")
    lookup_url_kwarg: str = "pk"
    serializer_class: UsersProjectsSerializer = UsersProjectsSerializer
    permission_classes: list = [IsAuthenticated & IsVerified & IsAdmin]


class JoiningRequestsViewSet(ModelViewSet):
    queryset: QuerySet = JoiningRequests.objects.all().order_by("-id")
    lookup_url_kwarg: str = "pk"
    serializer_class: JoiningRequestsSerializer = JoiningRequestsSerializer
    permission_classes: list = [IsAuthenticated & IsVerified & IsAdmin]
