from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    key = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)


class Page(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    version = models.IntegerField()
    content = models.TextField()
    created_date = models.DateTimeField()

    def repr(self):
        return {"id": self.id}


class WikiPage(Page):
    pass


class JournalPage(Page):
    date = models.DateTimeField()


class Task(models.Model):
    created_date = models.DateTimeField()
    due_date = models.DateTimeField()
    reporter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Reporter"
    )
    assignee = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Assignee"
    )
    content = models.TextField()
