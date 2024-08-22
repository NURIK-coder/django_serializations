from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from my_app.models import Note
from my_app.serializes import NoteSerializer


# Create your views here.

class NotesListView(APIView):
    def post(self, request, pk):
        # if request.data.get('username'):
        #     username = request.data['username']#если отправить FormData
        # username = request.POST['username']#если отправить JSON
        note = Note.objects.get(id=pk)
        note_serializer = NoteSerializer(note, data=request.data)
        if note_serializer.is_valid():
            note_serializer.save()
            # note = Note.objects.create(**note_serializer.data)
            # note = NoteSerializer(note)
            return Response(note.data)
        return Response({'Detail': 'Wrong data'}, status=422)

    def get(self, request):
        notes = Note.objects.all()

        notes_serializer = NoteSerializer(notes, many=True)
        return Response(notes_serializer.data)



# class NotesListView(ListAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
