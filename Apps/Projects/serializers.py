from django.db.models import Model
from rest_framework.serializers import ModelSerializer

from Projects.models import JoiningRequests, Project, UsersProjects


class UsersProjectsSerializer(ModelSerializer):

        class Meta:
            model: Model = UsersProjects
            fields: str = "__all__"


class ProjectSerializer(ModelSerializer):
        class Meta:
            model: Model = Project
            fields: str = "__all__"


class JoiningRequestsSerializer(ModelSerializer):

    class Meta:
        model: Model = JoiningRequests
        fields: str = "__all__"
