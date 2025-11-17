from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User,   
        on_delete=models.CASCADE, 
        related_name="tasks",
        null=True,
        blank=True
    )
    title = models.CharField(max_length=200)
    deadline = models.DateTimeField(null=True, blank=True)    
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Todo Task"
        verbose_name_plural = "Todo Tasks"
        ordering = ["-deadline"]

    def __str__(self):
        return self.title