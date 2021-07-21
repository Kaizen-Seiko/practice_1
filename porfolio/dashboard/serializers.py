from rest_framework import serializers
import sys
import os

# sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)).replace("porfolio\\porfolio", "porfolio\\info"))
from info.models import Education, Competence, Experience


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = "__all__"
