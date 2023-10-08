from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from django_mysql import status
from requests import Response
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from Projects.choices import RequestStatusChoices
from Projects.models import Project, UsersProjects, JoiningRequests
from Projects.permissions import IsProjectOwner
from Projects.serializers import ProjectSerializer, UsersProjectsSerializer, JoiningRequestsSerializer
from Users.permissions import IsAdmin
from Users.permissions import IsVerified


class ProjectViewSet(ModelViewSet):
    queryset: QuerySet = Project.objects.all().order_by("-id")
    lookup_url_kwarg: str = "pk"
    serializer_class: ProjectSerializer = ProjectSerializer
    permission_classes: list = [IsAuthenticated & IsVerified & IsProjectOwner]


class UsersProjectsViewSet(ModelViewSet):
    queryset: QuerySet = UsersProjects.objects.all().order_by("-id")
    lookup_url_kwarg: str = "pk"
    serializer_class: UsersProjectsSerializer = UsersProjectsSerializer
    permission_classes: list = [IsAuthenticated & IsVerified]


class JoiningRequestsViewSet(ModelViewSet):
    queryset: QuerySet = JoiningRequests.objects.all().order_by("-id")
    lookup_url_kwarg: str = "pk"
    serializer_class: JoiningRequestsSerializer = JoiningRequestsSerializer
    permission_classes: list = [IsAuthenticated & IsVerified]

    def update(self, request, *args, **kwargs):
        request = get_object_or_404(JoiningRequests, id=kwargs["pk"])
        if UsersProjects.objects.filter(user_id=request.user.id, project_id=request.project_id).exists():
            if request.data["status"] == RequestStatusChoices.ACCEPTED:
                UsersProjects.objects.create(
                    user_id=request.data["user_id"],
                    project_id=request.data["project_id"],
                    role=request.data["role"],
                )
            return super().update(request, *args, **kwargs)
        if self.get_object().user_id == request.user.id:
            return super().update(request, *args, **kwargs)
        raise PermissionDenied("You don't have permission")

    def destroy(self, request, *args, **kwargs):
        if self.get_object().user_id == request.user.id:
            return super().destroy(request, *args, **kwargs)
        raise PermissionDenied("You don't have permission")

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsAuthenticated & IsVerified],
        url_path='(projects/?P<project_id>[^/.]+)'
    )
    def list_by_project(self, request, project_id):
        if UsersProjects.objects.filter(user_id=request.user.id, project_id=project_id).exists():
            self.queryset = JoiningRequests.objects.filter(project_id=project_id).all()
            return super().list(request)
        raise PermissionDenied("You don't have permission")