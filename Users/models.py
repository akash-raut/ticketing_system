from django.db import models
from Projects.models import Project


STATUS_CHOICES = (
    (0, "INACTIVE"),
    (1, "ACTIVE"),
)


class Staff_User(models.Model):
    ''' Holds staff user fields '''
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    project_assigned = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "staff_users"

