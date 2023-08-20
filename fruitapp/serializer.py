from rest_framework import serializers

from fruitapp.models import Image, Prediction, Results


class PredictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prediction
        fields = '__all__'


class ResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Results
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'