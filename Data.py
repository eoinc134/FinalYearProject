import csv
import random

from pymzn import dzn

##PARAMETERS##
NUM_SUPERVISORS = 20
NUM_STUDENTS = 100

TIMESLOTS = 8
SESSIONS = 3

MAX_STUDENTS_PER_SESSION = 6
MAX_STUDENTS_PER_SUPERVISOR = 7
MAX_SUPERVISORS_PER_SESSION = 4
MIN_SUPERVISORS_PER_SESSION = 2

NEW_DATA_FILE = True
#############
CSV_FILE = "./data/availability.csv"


class Data:
    def generate_availability():
        with open(CSV_FILE, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write X rows with randomly assigned attributes (70% chance of being True)
            for i in range(1, NUM_SUPERVISORS+1):
                row = [random.choices(['true', 'false'], weights=(0.7, 0.3))[0] for j in range(TIMESLOTS)]
                writer.writerow(row)

        
    def get_availability_data():
        # Generate new availability lists
        if(NEW_DATA_FILE):
            Data.generate_availability()

        # Return availability data 
        with open(CSV_FILE) as file_name:
            file_read = csv.reader(file_name)
            array = list(file_read)
        return array

    def generate_data_file(dataFile):
        # Get Supervisor Availability Data
        availability = Data.get_availability_data()

        # Load all data
        data = {
            "students": NUM_STUDENTS,
            "supervisors": NUM_SUPERVISORS,

            "timeslots": TIMESLOTS,
            "sessions": SESSIONS,       

            "max_students_per_session": MAX_STUDENTS_PER_SESSION,
            "max_students_per_supervisor": MAX_STUDENTS_PER_SUPERVISOR,
            "max_supervisors_per_session": MAX_SUPERVISORS_PER_SESSION,
            "min_supervisors_per_session": MIN_SUPERVISORS_PER_SESSION,

            "availability": availability,
        }

        # Write to .dzn file
        with open(dataFile, 'w') as outfile:
            outfile.write("\n".join(dzn.dict2dzn(data)))