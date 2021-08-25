from rest_framework import serializers
from .models import Student

# validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('name start with r')
    #this validation applying on name so we wite few line of code in name
    

class StudentSerializer(serializers.Serializer):
    #id = serializers.IntegerField()
    name = serializers.CharField(validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField()
    
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
# field level validation
    def validate_roll(self, value):
        if value >=1000:
            raise serializers.ValidationError('seat full')
        return value
# object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'a' and ct.lower() !='abc':
            raise serializers.ValidationError('city must abc')
        return data