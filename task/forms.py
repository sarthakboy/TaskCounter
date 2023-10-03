from django import forms
from .models import TaskInput as TaskInputModel

class TaskInputForm(forms.ModelForm):

    class Meta:
        model = TaskInputModel
        exclude = ['dayToGo']  # Exclude the 'daytogo' field

    # Optionally, you can add any custom validation or widgets for other fields here
