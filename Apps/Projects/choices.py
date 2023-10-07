from django.db.models import TextChoices

class StatusChoices(TextChoices):
    OPEN: tuple = ("OP", "Open to contributions") #The project is actively accepting contributions.
    ACTIVE_OPEN: tuple = ("AO", "Active and Open") #The project is actively being developed and actively accepting contributions.
    ACTIVE: tuple = ("AC", "Active") #The project is actively accepting contributions.
    INACTIVE: tuple = ("I", "Inactive") #The project is not currently in development and does not accept contributions at this time.
    COMPLETED: tuple = ("C", "Completed") #The project has achieved its goals and is considered finished.
    ARCHIVED: tuple = ("AR", "Archived") #The project has been archived and is no longer active.
    ON_HOLD: tuple = ("OH", "On-Hold") #The project has been temporarily paused due to issues or lack of resources.
