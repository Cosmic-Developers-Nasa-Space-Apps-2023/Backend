from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.permissions import BasePermission

from Projects.models import Project


class IsProjectOwner(BasePermission):
    message: str = "You don't have permission"

    def has_permission(self, request: HttpRequest, view: View) -> bool:
        if request.method == "GET":
            return True
        try:
            pk: int = request.parser_context["kwargs"]["pk"]
            project: Project = get_object_or_404(Project, id=pk)
        except Exception as e:
            return False
        return request.user.id == project.owner.id
