from django.urls import path

from my_app.views import NotesListView

urlpatterns = [
    path('index/', NotesListView.as_view())
]