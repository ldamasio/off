from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from .models import Item
from .serializer import ItemSerializer
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from datetime import datetime
import requests
import json

@api_view(['GET'])
def ApiOverview(request):
    start_time = settings.SERVER_START
    now = datetime.now()
    online_time = now - start_time
    online_time = online_time.total_seconds() / 60
    response = requests.get('http://localhost:8002/ht/?format=json')
    bytes_response = response.content
    decode_response = bytes_response.decode('utf8')
    json_value = json.loads(decode_response)
    api_urls = {
        'Listagem paginada de todos os itens': '/products',
        'Mostra detalhes de item filtrado por código': '/products/code',
        'Adiciona': '/create',
        'Atualiza produto com determinado código': '/products/code (método PUT)',
        'Deleta produto com determinado código': '/procuts/code (método DELETE)',
        'Conexão com Banco de dados (Leitura e escrita)': json_value['DatabaseBackend'],
        'Horário de último cronjob': 'Não há cronjobs neste projeto',
        'Tempo online': str(round(online_time, 2)) + ' minutos',
        'Uso de memória': json_value['MemoryUsage'],
    }
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ViewItem(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        return self.queryset.filter(code=self.kwargs['pk'])

@api_view(['PUT'])
def update_items(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
