from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id','movie','user','created_at']



    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError(
                "Rating must be between 1 and 10."
            )
        return value