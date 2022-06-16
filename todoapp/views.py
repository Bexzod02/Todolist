from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoForm
from .models import Todo, Logo
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user
    todos = Todo.objects.filter(author=user).order_by('-update_at')
    logo = Logo.objects.all().last()
    q = request.GET.get('q')
    if q:
        todos = todos.filter(status__exact=int(q))
    ctx = {
        'todos': todos,
        'logo':logo
    }
    return render(request, 'index.html', ctx)


@login_required
def single(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        messages.success(request, 'successfully updated !!')
        return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'single.html', ctx)

def search(request):
    obj = None
    if request.method == 'POST':
        query = request.POST.get('qy')
        obj = Todo.objects.search(query)
        if not obj:
            messages.error(request, ('Is not defined items !!!'))
            return redirect('/')
    context={
            'object':obj
    }
    return render(request, 'search.html', context)

def delete(request, pk):
    obj = get_object_or_404(Todo ,id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.info(request, ('Succesful delete item !!!'))
        return redirect('/')
    return render(request, 'delete.html', {'obj':obj})

def create(request):
    user = request.user
    form = TodoForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = user
        obj.save()
        messages.success(request, 'successfully created')
        return redirect('/')
    return render(request, 'single.html', {'form': form})
