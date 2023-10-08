from django.db.models import Model
from django.shortcuts import get_object_or_404
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from Projects.models import JoiningRequests, Project, UsersProjects
from Users.models import User
from Users.serializers import UserSerializer


class UsersProjectsSerializer(ModelSerializer):

        class Meta:
            model: Model = UsersProjects
            fields: str = "__all__"


class ProjectSerializer(ModelSerializer):
    owner = SerializerMethodField()

    def get_owner(self, obj, *args, **kwargs):
        user = get_object_or_404(User, id=obj.owner.id)
        return UserSerializer(user).data

    class Meta:
        model: Model = Project
        fields: str = "__all__"


class JoiningRequestsSerializer(ModelSerializer):
    user = SerializerMethodField(read_only=True)

    def get_user(self, obj, *args, **kwargs):
        user = get_object_or_404(User, id=obj.user_id.id)
        return UserSerializer(user).data

    class Meta:
        model: Model = JoiningRequests
        fields: str = ["id", "project_id", "desired_role", "status", "working_date", "summary", "user_id", "user"]