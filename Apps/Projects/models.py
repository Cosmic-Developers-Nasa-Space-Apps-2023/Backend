from django.db.models import Model, TextField, JSONField, DateField, CharField, BooleanField, ManyToManyField, \
    ForeignKey, CASCADE
from Users.models import User
from Projects.choices import StatusChoices, RequestStatusChoices
from Users.models import User


class Project(Model):
    title = TextField(
        "title",
        null=False,
        blank=False
    )
    description = TextField(
        "description",
        null=False,
        blank=False
    )
    desired_skills = JSONField(
        "DesiredSkills",
        null=True,
        blank=True        
    )
    field = CharField(
        "field",
        max_length=100,
        null=False,
        blank=False
    )
    status = CharField(
        "status",
        max_length=100,
        choices=StatusChoices.choices,
        default=StatusChoices.OPEN,
        null=True,
    )
    owner = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="owner"
    )
    starting_date = DateField(null=False)
    finishing_date = DateField(null=True)


class UsersProjects(Model):
    user_id = ManyToManyField(
        User,
        related_name="users"
    )
    project_id = ManyToManyField(
        Project,
        related_name="projects"
    )
    role = TextField(
        "role",
        null=False,
        blank=False
    )


class JoiningRequests(Model):
    user_id = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="user"
    )
    project_id = ForeignKey(
        Project,
        on_delete=CASCADE,
        related_name="project"
    )
    status = CharField(
        "status",
        max_length=100,
        choices=RequestStatusChoices.choices,
        default=RequestStatusChoices.PENDING,
        null=True,
    )
    desired_role = CharField(
        "desired_role",
        max_length=100,
        null=False,
        blank=False
    )
    working_date = DateField(null=False)
    summary = TextField(
        "summary",
        max_length=500
    )
