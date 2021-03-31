from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.filter(user=request.user)

    context = {
        'notes':notes
    }
    return render(request, 'templates/note/note_list.html', context)


def add_note(request):
    form = NoteForm()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            print('note is valid')
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, 'Notes saved successfully.')
            return redirect('notelist')
        else:
            messages.warning('Notes save failed ')

    context = {
        'form':form
    }
    return render(request, 'templates/note/add_note.html', context)

def edit_note(request, id):
    note = Note.objects.get(id=id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            messages.success(request, 'Note is updated.')
            return redirect('notelist')

        else:
            messages.warning(request, 'Note update failed.')

    context = {
        'note': note
    }
    return render(request, 'templates/note/edit_note.html', context)


def view_note(request, id):
    note = Note.objects.get(id=id)

    context = {
        'note': note
    }
    return render(request, 'templates/note/view_note.html', context)



def delete_note(request, id):
    if request.method == 'POST':
        delete_note = Note.objects.get(id=id)
        delete_note.delete()
        messages.success(request, 'Note deleted')
    else:
        messages.warning(request, 'Note delete fail')
    
    return redirect('notelist')
