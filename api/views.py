from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer, ItemCreateSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return ItemCreateSerializer
        return ItemSerializer