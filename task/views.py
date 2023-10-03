from django.shortcuts import render, redirect
from .forms import TaskInputForm
from .models import TaskInput  # Import TaskInput model, not Task

def index(request):
    if request.method == 'POST':
        form = TaskInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskInputForm()
    
    # Retrieve all tasks from the database using the TaskInput model
    tasks = TaskInput.objects.all()
    
    return render(request, "index.html", {'form': form, 'tasks': tasks})


from django.shortcuts import redirect, get_object_or_404
from .models import TaskInput

def delete_task(request, task_id):
    task = get_object_or_404(TaskInput, pk=task_id)
    task.delete()
    return redirect('index')  # Redirect to the task list page after deletion

from django.http import JsonResponse

def increase_day_to_go(request, task_id):
    try:
        task = TaskInput.objects.get(pk=task_id)
        task.dayToGo += 1
        task.save()
        return JsonResponse({'updatedDayToGo': task.dayToGo})
    except TaskInput.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)
