from rest_framework import serializers


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value['duration'] > 120:
            raise serializers.ValidationError(
                'Длительность привычки не может быть больше 120 секунд'
            )
        
        
        if value['is_good']:
            if value['related'] or value['prize']:
                raise serializers.ValidationError(
                    'У приятной привычки не может быть связанной привычки или вознаграждения'
                )
            if value['related'] and value['prize']:
                raise serializers.ValidationError(
                    'Может быть либо связанная привычка, либо вознаграждение, но не оба сразу'
                )
            if value['related']:
                if not value['related'].is_good:
                    raise serializers.ValidationError(
                        'Связанные привычки должны быть приятными'
                    )
