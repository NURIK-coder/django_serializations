from rest_framework import serializers

from my_app.models import Note


# class NotesSerializer(serializers.Serializer):
#     title = serializers.CharField(allow_null=True)
#     description = serializers.CharField(allow_null=True)


class NoteSerializer(serializers.ModelSerializer):
    # description = serializers.CharField(write_only=True) #переопределение Когда serializers.Serializer


    class Meta:
        model = Note
        fields = ['id', 'title', 'description', 'created_at']
        # extra_kwargs = {
        #     'description': {
        #         'write_only': True
        #     }
        # }#переопределение Когда serializers.ModelSerializer
