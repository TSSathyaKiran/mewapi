import csv
import os
from django.core.management.base import BaseCommand
from api.models import Pokemon
from django.conf import settings

class Command(BaseCommand):
    help = "Loads Pokemon data from a CSV file into the database."

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(settings.BASE_DIR, "pokedex.csv")

        if not os.path.exists(csv_path):
            self.stdout.write(self.style.ERROR(f"CSV file not found at: {csv_path}"))
            return

        self.stdout.write("Starting data loading...")
        
        try:
            with open(csv_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                records_created = 0

                for row in reader:
                    if "image_path" in row:
                        del row["image_path"]

                    cleaned_data = {k: (None if v == "" or v == "nan" else v) for k, v in row.items()}
                    
                    boolean_fields = [
                        'is_paldean', 'is_hisuian', 'is_galarian', 'is_alolan', 
                        'is_mega', 'is_gigantamax', 'is_partner', 'has_form_difference', 
                        'is_forme_change'
                    ]
                    for field in boolean_fields:
                        cleaned_data[field] = bool(int(cleaned_data[field]))

                    integer_fields = [
                        'catch_rate', 'base_friendship', 'base_experience', 'egg_cycles'
                    ]
                    for field in integer_fields:
                        if cleaned_data[field] is not None:
                            cleaned_data[field] = int(float(cleaned_data[field]))
                        else:
                            cleaned_data[field] = 0

                    if not cleaned_data.get("ability_1"):
                        cleaned_data["ability_1"] = "Unknown"

                    Pokemon.objects.create(**cleaned_data)
                    records_created += 1

            self.stdout.write(self.style.SUCCESS(f"Successfully loaded {records_created} records."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
            self.stdout.write(self.style.ERROR("Data loading failed."))
