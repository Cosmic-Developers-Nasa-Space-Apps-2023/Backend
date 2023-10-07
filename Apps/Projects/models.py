from django.db.models import Model, TextField, JSONField, DateField, CharField, BooleanField, ManyToManyField
from Users.models import User
from Projects.choices import StatusChoices
<<<<<<< Updated upstream
from Users.models import User
=======
>>>>>>> Stashed changes


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
    field = JSONField(
        "field",
        null=True,
        blank=True
    )
    status = CharField(
        "status",
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.OPEN,
        null=True,
    )
    starting_date = DateField(null=False)
    finishing_date = DateField(null=True)

class UsersProjects(Model):
    user_id = ManyToManyField(
        User,
        related_name="users_projects"
    )
    project_id = ManyToManyField(
        Project,
        related_name="users_projects"
    )
    role = TextField(
        "role",
        null=False,
        blank=False
    )
    scope = TextField(
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
    working_date = DateField(null=False)
    summary = TextField(
        "summary",
        max_length=500
    )