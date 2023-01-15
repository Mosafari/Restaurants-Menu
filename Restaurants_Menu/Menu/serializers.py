from rest_framework import serializers
from .models import Menu, User


class MenuSerializer(serializers.ModelSerializer):
    
    # is_my_object = serializers.SerializerMethodField('_is_my_find')
    
    # def _is_my_find(self, obj):
    #     self.user = self.context.get("user")
        
    class Meta:
        model = Menu
        fields = ["name", "price", "categories", "details"]
        
    # def __init__(self, user, **kwargs):
    #     self.user = user
    #     super().__init__(self, **kwargs) 
           
    def create(self, validated_data):
        print(self.context.get("user"),validated_data,validated_data.get('name'))
        menu = Menu.objects.create(name=validated_data.get('name'),
                                       price = float(validated_data['price']),
                                       categories = validated_data['categories'],
                                       details = validated_data['details'],
                                       restaurant = User.objects.filter(email=self.context.get("user"))[0],
                                         )
        menu.save()
        return menu