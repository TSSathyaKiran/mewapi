# MewAPI — Pokémon REST API

MewAPI is a Django REST Framework–based Pokédex API.  
It allows you to search, filter, and sort detailed Pokémon data for use in applications, games, or research projects.

---

## Features

- List all Pokémon in the database.
- Search by:
  - Name
  - Type 1 / Type 2
  - Species
  - Status (e.g., Legendary, Mythical, Normal)
  - Generation
- Sort by:
  - Pokédex Number
  - Name
  - Total Points
  - HP
  - Attack
  - Defense
  - Speed
- Retrieve complete Pokémon details including:
  - Regional forms
  - Typing
  - Physical traits
  - Abilities
  - Stats
  - Capture/growth information
  - Breeding details
  - Type effectiveness
- JSON responses for easy integration.

---

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/TSSathyaKiran/mewapi.git
cd mewapi
```

### Install Requirements
```bash
pip install -r requirements.txt
```

### Run the Development Server
```bash
python manage.py runserver
```

The API will be available at:
```
http://127.0.0.1:8000/api/pokemon/
```

---

## API Endpoints

### List All Pokémon
```http
GET /api/pokemon/
```
Returns a paginated list of Pokémon.

### Retrieve a Single Pokémon
```http
GET /api/pokemon/{id}/
```
Example:
```
GET /api/pokemon/25/
```

### Search Pokémon
Search by the following fields:
- name
- type_1
- type_2
- species
- status
- generation

Example:
```
GET /api/pokemon/?search=Fire
GET /api/pokemon/?search=Charizard
```

### Sorting
Sort results using the `ordering` parameter:

| Field            | Example                  | Description                    |
|------------------|--------------------------|---------------------------------|
| pokedex_number   | `?ordering=pokedex_number` | Sort by Pokédex number (asc)   |
| name             | `?ordering=name`           | Sort alphabetically (asc)      |
| total_points     | `?ordering=-total_points`  | Sort by total points (desc)    |
| hp               | `?ordering=-hp`            | Sort by HP (desc)              |
| attack           | `?ordering=-attack`        | Sort by Attack (desc)          |
| defense          | `?ordering=-defense`       | Sort by Defense (desc)         |
| speed            | `?ordering=-speed`         | Sort by Speed (desc)           |

Example:
```
GET /api/pokemon/?ordering=-attack
```

### Combining Search and Sort
Example:
```
GET /api/pokemon/?search=Electric&ordering=-speed
```

---

## Example Response
```json
{
    "pokedex_number": 25,
    "name": "Pikachu",
    "generation": 1,
    "status": "Normal",
    "species": "Mouse Pokémon",
    "is_paldean": false,
    "is_hisuian": false,
    "is_galarian": false,
    "is_alolan": false,
    "is_mega": false,
    "is_gigantamax": false,
    "is_partner": false,
    "has_form_difference": false,
    "is_forme_change": false,
    "type_number": 1,
    "type_1": "Electric",
    "type_2": null,
    "height_m": 0.4,
    "weight_kg": 6.0,
    "abilities_number": 2,
    "ability_1": "Static",
    "ability_2": null,
    "ability_hidden": "Lightning Rod",
    "total_points": 320,
    "hp": 35,
    "attack": 55,
    "defense": 40,
    "sp_attack": 50,
    "sp_defense": 50,
    "speed": 90,
    "catch_rate": 190,
    "base_friendship": 70,
    "base_experience": 112,
    "growth_rate": "Medium Fast",
    "egg_type_number": 1,
    "egg_type_1": "Field",
    "egg_type_2": "Fairy",
    "percentage_male": 50.0,
    "egg_cycles": 10,
    "against_normal": 1.0,
    "against_fire": 1.0,
    "against_water": 1.0,
    "against_electric": 0.5,
    "against_grass": 1.0,
    "against_ice": 1.0,
    "against_fight": 1.0,
    "against_poison": 1.0,
    "against_ground": 2.0,
    "against_flying": 0.5,
    "against_psychic": 1.0,
    "against_bug": 1.0,
    "against_rock": 1.0,
    "against_ghost": 1.0,
    "against_dragon": 1.0,
    "against_dark": 1.0,
    "against_steel": 0.5,
    "against_fairy": 1.0
}
```

---
