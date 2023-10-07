from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.db.models import Model

from Projects.models import Project, UsersProjects, JoiningRequests


class ProjectAdmin(ModelAdmin):
    model: Model = Project
    list_display: tuple = ("id", "title", "status")
    list_display_links: tuple = ("id", "title")
    list_filter: tuple = (
        "title",
        "status",
        "field"
    )
    fieldsets: tuple = (
        ("Basic", {"fields": ("id", "title", "description", "field")}),
        ("Dates", {"fields": ("starting_date", "finishing_date")}),
        ("Requests", {"fields": ("status", "desired_skills")}),
    )
    readonly_fields: list = [
        "id",
    ]
    search_fields: tuple = ("title", "id")


class UsersProjectsAdmin(ModelAdmin):
    model: Model = UsersProjects
    list_display: tuple = ("id", "role", "scope")
    list_display_links: tuple = ("id",)
    list_filter: tuple = (
        "user_id",
        "project_id",
        "role",
        "scope"
    )
    fieldsets: tuple = (
        ("Basic", {"fields": ("id", "user_id", "project_id", "role", "scope")}),
    )
    readonly_fields: list = [
        "id",
    ]
    search_fields: tuple = ("id", "user_id", "project_id", "role", "scope")


class JoiningRequestAdmin(ModelAdmin):
    model: Model = JoiningRequests
    list_display: tuple = ("id", "summary", "status")
    list_display_links: tuple = ("id",)
    list_filter: tuple = (
        "user_id",
        "project_id",
        "status",
        "working_date"
    )
    fieldsets: tuple = (
        (
            "Basic", {
                "fields": (
                    "id", "user_id", "project_id", "summary", "status", "working_date"
                )
            }
        ),
    )
    readonly_fields: list = [
        "id",
    ]
    search_fields: tuple = (
        "id", "user_id", "project_id", "summary", "status", "working_date"
    )


admin.site.register(Project, ProjectAdmin)
admin.site.register(UsersProjects, UsersProjectsAdmin)
admin.site.register(JoiningRequests, JoiningRequestAdmin)
