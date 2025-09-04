from django.contrib import admin

from django.contrib import admin
from .models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('pokedex_number', 'name', 'generation', 'status', 'type_1', 'type_2')
    list_filter = ('generation', 'status', 'type_1', 'type_2', 'is_paldean', 'is_hisuian', 'is_galarian', 'is_alolan')
    search_fields = ('name', 'pokedex_number')
    ordering = ('pokedex_number',)
    fieldsets = (
        ('Basic Info', {
            'fields': ('pokedex_number', 'name', 'generation', 'status', 'species')
        }),
        ('Regions', {
            'fields': ('is_paldean', 'is_hisuian', 'is_galarian', 'is_alolan', 'is_mega', 'is_gigantamax', 'is_partner', 'has_form_difference', 'is_forme_change')
        }),
        ('Typing', {
            'fields': ('type_number', 'type_1', 'type_2')
        }),
        ('Physical Traits', {
            'fields': ('height_m', 'weight_kg')
        }),
        ('Abilities', {
            'fields': ('abilities_number', 'ability_1', 'ability_2', 'ability_hidden')
        }),
        ('Stats', {
            'fields': ('total_points', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed')
        }),
        ('Capture/Growth', {
            'fields': ('catch_rate', 'base_friendship', 'base_experience', 'growth_rate')
        }),
        ('Breeding', {
            'fields': ('egg_type_number', 'egg_type_1', 'egg_type_2', 'percentage_male', 'egg_cycles')
        }),
        ('Type Effectiveness', {
            'fields': (
                'against_normal', 'against_fire', 'against_water', 'against_electric', 'against_grass', 'against_ice',
                'against_fight', 'against_poison', 'against_ground', 'against_flying', 'against_psychic', 'against_bug',
                'against_rock', 'against_ghost', 'against_dragon', 'against_dark', 'against_steel', 'against_fairy'
            )
        }),
    )
