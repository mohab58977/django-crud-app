from django.forms import ModelForm
from .models import project


class ProjectForm(ModelForm):
    class Meta:
        model = project
        fields = [
            "title",
            "details",
            "start_date",
            "end_date",
            "id",
            "owner",
        ]
