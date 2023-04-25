from django.shortcuts import render, redirect
from .models import Task, Priority
from .forms import TaskForm


def get_tasks():
    return Task.objects.order_by('creation_date')


def tasks_index(request):
    tasks_list = get_tasks()
    return render(request, 'tasks/tasks_index.html', {'tasks_list': tasks_list})


def task_create(request):
    tasks_list = get_tasks()
    
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if not task_form.is_valid():
           return render(request, 'tasks/task_create.html', {'tasks_list': tasks_list,
                                                             'task_form': task_form,
                                                             }
                         )
        
        task_form.save()
        return redirect('tasks_index')

    task_form = TaskForm()
    return render(request, 'tasks/task_create.html', {'tasks_list': tasks_list,
                                                      'task_form': task_form,
                                                      }
                  )


def task_detail(request, pk):
    tasks_list = get_tasks()
    task = Task.objects.get(pk=pk)

    return render(request, 'tasks/task_detail.html', {'tasks_list': tasks_list,
                                                      'task': task,
                                                      }
                  )
    

def task_edit(request, pk):
    tasks_list = get_tasks()
    task = Task.objects.get(pk=pk)
    
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if not task_form.is_valid():
            return render(request, 'tasks/task_edit.html', {'tasks_list': tasks_list,
                                                            'task_form': task_form,
                                                            'task': task,
                                                            }
                          )

        task_form.save()
        return redirect('task_detail', pk=pk)

    task_form = TaskForm(instance=task)
    return render(request, 'tasks/task_edit.html', {'tasks_list': tasks_list,
                                                    'task_form': task_form,
                                                    'task': task,
                                                    }
                  )
   

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    
    return redirect('tasks_index')


# def task_search(request):
#     tasks_list = get_tasks()
#     pass


def priority_new(request):
    if request.method == 'POST':
        Priority.objects.create(level=request.POST['priority'])
        return redirect('tasks_index')
        
    return render(request, 'tasks/priority_new.html')

