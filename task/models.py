from django.db import models

class TaskInput(models.Model):
    task = models.TextField()
    dayGoal = models.IntegerField()
    dayToGo = models.IntegerField(default=0)  # Set the default value to 0

    def __str__(self):
        return self.task
