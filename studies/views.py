from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm

def main_view(request):
    studies = Study.objects.all()
    return render(request, 'main_view.html', {'studies': studies})

def open(request, id):
    data = Study.objects.get(id=id)
    return render(request, 'photo.html',{'study':data})

def add_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_view')
    else:
        form = StudyForm()
    return render(request, 'add_study.html', {'form': form})

def view_study(request, study_id):
    study = get_object_or_404(Study, pk=study_id)
    return render(request, 'view_study.html', {'study': study})

def edit_study(request, study_id):
    study = get_object_or_404(Study, pk=study_id)
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('main_view')
    else:
        form = StudyForm(instance=study)
    return render(request, 'edit_study.html', {'form': form, 'study': study})

def delete_study(request, study_id):
    study = get_object_or_404(Study, pk=study_id)
    study.delete()
    return redirect('main_view')
