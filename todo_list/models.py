from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    relevant_tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["done", "-created_at"]

    def __str__(self):
        return self.content
