import csv
import random


class Availability:
    def generate_availability(filename):
            attributes = ['attribute1', 'attribute2', 'attribute3', 'attribute4', 'attribute5', 'attribute6', 'attribute7', 'attribute8']
        
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                
                # Write header row with attribute names
                writer.writerow(['Name'] + attributes)
                
                # Write 20 rows with randomly assigned attributes (60% chance of being True)
                for i in range(1, 21):
                    row = [f'Person{i}'] + [random.choices([True, False], weights=(0.6, 0.4))[0] for j in range(8)]
                    writer.writerow(row)
            
            print(f'Successfully created {filename}!')