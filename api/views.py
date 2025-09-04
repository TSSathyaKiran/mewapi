from rest_framework import viewsets, filters
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by("pokedex_number")
    serializer_class = PokemonSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "type_1", "type_2", "species", "status", "generation"]
    ordering_fields = ["pokedex_number", "name", "total_points", "hp", "attack", "defense", "speed"]
