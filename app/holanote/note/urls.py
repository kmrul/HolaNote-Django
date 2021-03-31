from django.urls import path
from .views import note_list, add_note, edit_note, view_note, delete_note

urlpatterns = [
    path('list/', note_list, name='notelist' ),
    path('new/', add_note, name='addnote'),
    path('view/<int:id>', view_note, name='viewnote'),
    path('edit/<int:id>', edit_note, name='editnote'),
    path('delete/<int:id>', delete_note, name='deletenote'),
]