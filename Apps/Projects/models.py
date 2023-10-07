from django.db.models import Model, TextField, JSONField, DateField, CharField, BooleanField, ManyToManyField
from Apps.Users.models import User
from Projects.choices import StatusChoices
import pycountry

# Create your models here.

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
        max_length=1,
        choices=StatusChoices.choices,
        default=StatusChoices.OPEN,
        null=True,
    )
    starting_date = DateField(null=False)
    finishing_date = DateField(null=True)

class UsersProjects(Model):
    user_id = CharField(
        "UserID",
        null=False,
        blank=False
    )
    project_id = CharField(
        "ProjectID",
        null=False,
        blank=False
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

class Users(Model):
    id = CharField(
        "ID",
        null=False,
        blank=False
    )
    username = TextField(
        "username",
        null=False,
        blank=False
    )
    first_name = TextField(
        "FirstName",
        null=False,
        blank=False
    )
    last_name = TextField(
        "LastName",
        null=False,
        blank=False
    )
    email = TextField(
        "email",
        null=False,
        blank=False
    )
    skills = JSONField(
        "skills",
        null=True,
        blank=True        
    )
    experience = JSONField(
        "DesiredSkills",
        null=False,
        blank=False        
    )
    countryChoices = list(pycountry.countries)
    country = CharField(
        "country",
        max_length=1,
        choices=countryChoices,
        null=False,
    )
    is_verified = BooleanField(default=False, editable=True)
    seeking_fields = JSONField(
        "SeekingSkills",
        null=True,
        blank=True        
    )
    working_availability = DateField(null=True)
    defaultSummary = TextField(
        "DefaultSummary",
        max_length=500,
        null=False,
        blank=False
    )
    is_public = BooleanField(default=False, editable=True)

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
        max_length=500,
        default=Users.defaultSummary
    )