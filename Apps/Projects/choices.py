from django.db.models import TextChoices


class StatusChoices(TextChoices):
    OPEN: tuple = ("OP", "Open to contributions")
    ACTIVE_OPEN: tuple = ("AO", "Active and Open")
    ACTIVE: tuple = ("AC", "Active")
    INACTIVE: tuple = ("I", "Inactive")
    COMPLETED: tuple = ("C", "Completed")
    ARCHIVED: tuple = ("AR", "Archived")
    ON_HOLD: tuple = ("OH", "On-Hold")


class RequestStatusChoices(TextChoices):
    PENDING: tuple = ("P", "Pending")
    ACCEPTED: tuple = ("A", "Accepted")
    REJECTED: tuple = ("R", "Rejected")