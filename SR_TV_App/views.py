from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.contrib import messages

def index(request):
    return redirect(shows)

def shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request,'shows.html',context)

def show_form(request):
    return render(request,'show_form.html')

def add_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(show_form)
    else:
        show = Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date = request.POST['release_date'],
            description = request.POST['description']
        )
        messages.success(request, "Show successfully added")
        id = show.id
        return redirect(f"/shows/{show.id}")

def this_show(request,id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request,'this_show.html',context)

def update_show_form(request,id):
    context = {
    'show' : Show.objects.get(id=id)
    }
    return render(request, 'edit_this_show.html',context)

def submit_update(request,id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f'/shows/{id}/edit')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        messages.success(request, "Show successfully updated")
        id = show.id
        return redirect(f"/shows/{show.id}")

def delete_show(request, id):
    current_show = Show.objects.get(id=id)
    current_show.delete()
    return redirect('/')



