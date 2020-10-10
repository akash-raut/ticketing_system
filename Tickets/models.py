from django.db import models
from Users.models import Staff_User
from django.contrib.auth.models import User


STATUS_CHOICES = (
    (0, "DRAFT"),
    (1, "ONGOING"),
    (2, "COMPLETED"),
    (3, "ARCHIVED"),
)


class Ticket(models.Model):
    ''' Covers fields for tickets '''
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    attachment = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tickets"


