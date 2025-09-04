from django.db import models

class Pokemon(models.Model):
    pokedex_number = models.IntegerField()
    name = models.CharField(max_length=100)
    generation = models.IntegerField()
    status = models.CharField(max_length=50) 
    species = models.CharField(max_length=100)

    # Regionals
    is_paldean = models.BooleanField(default=False)
    is_hisuian = models.BooleanField(default=False)
    is_galarian = models.BooleanField(default=False)
    is_alolan = models.BooleanField(default=False)
    is_mega = models.BooleanField(default=False)
    is_gigantamax = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)
    has_form_difference = models.BooleanField(default=False)
    is_forme_change = models.BooleanField(default=False)

    # Typing
    type_number = models.IntegerField()
    type_1 = models.CharField(max_length=50)
    type_2 = models.CharField(max_length=50, null=True, blank=True)

    # Physical traits
    height_m = models.FloatField()
    weight_kg = models.FloatField()

    # Abilities
    abilities_number = models.IntegerField()
    ability_1 = models.CharField(max_length=100)
    ability_2 = models.CharField(max_length=100, null=True, blank=True)
    ability_hidden = models.CharField(max_length=100, null=True, blank=True)

    # Stats
    total_points = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()

    # Capture / growth
    catch_rate = models.IntegerField()
    base_friendship = models.IntegerField()
    base_experience = models.IntegerField()
    growth_rate = models.CharField(max_length=50)

    # Breeding
    egg_type_number = models.IntegerField()
    egg_type_1 = models.CharField(max_length=50)
    egg_type_2 = models.CharField(max_length=50, null=True, blank=True)
    percentage_male = models.FloatField(null=True, blank=True)
    egg_cycles = models.IntegerField()

    # Type effectiveness
    against_normal = models.FloatField()
    against_fire = models.FloatField()
    against_water = models.FloatField()
    against_electric = models.FloatField()
    against_grass = models.FloatField()
    against_ice = models.FloatField()
    against_fight = models.FloatField()
    against_poison = models.FloatField()
    against_ground = models.FloatField()
    against_flying = models.FloatField()
    against_psychic = models.FloatField()
    against_bug = models.FloatField()
    against_rock = models.FloatField()
    against_ghost = models.FloatField()
    against_dragon = models.FloatField()
    against_dark = models.FloatField()
    against_steel = models.FloatField()
    against_fairy = models.FloatField()

    def __str__(self):
        return f"{self.name} (#{self.pokedex_number})"
