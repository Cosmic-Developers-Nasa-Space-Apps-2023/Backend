from django.db.models import Model, TextField, JSONField, DateField, CharField, BooleanField, ManyToManyField
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
    user_id = ManyToManyField(
        User,
        related_name="joining_requests"
    )
    project_id = ManyToManyField(
        Project,
        related_name="joining_requests"
    )
    status = CharField(
        "status",
        max_length=100,
        choices=RequestStatusChoices.choices,
        default=RequestStatusChoices.PENDING,
        null=True,
    )
    working_date = DateField(null=False)
    summary = TextField(
        "summary",
        max_length=500
    )
