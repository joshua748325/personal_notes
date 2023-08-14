from django.urls import path

from .views import NoteList, CreateNote, ReadNote, UpdateNote, DeleteNote, StarNote, StarNoteList

app_name='note'
urlpatterns = [
    path('',NoteList.as_view(),name='home'),
    path('note/starred/',StarNoteList.as_view(),name='starred'),
    path('note/create/',CreateNote.as_view(),name='create_note'),
    path('note/<int:pk>/',ReadNote.as_view(),name='read_note'),
    path('note/<int:pk>/update/',UpdateNote.as_view(),name='update_note'),
    path('note/<int:pk>/delete/',DeleteNote.as_view(),name='delete_note'),
    path('note/<int:pk>/star/',StarNote.as_view(),name='star_note'),
]