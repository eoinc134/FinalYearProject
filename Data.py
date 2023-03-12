import csv
import random

from pymzn import dzn

##CONSTANTS##
NUM_SUPERVISORS = 20
NUM_STUDENTS = 100

TIMESLOTS = 8
SESSIONS = 3

MAX_STUDENTS_PER_SESSION = 6
MAX_STUDENTS_PER_SUPERVISOR = 7
MAX_SUPERVISORS_PER_SESSION = 6
MIN_SUPERVISORS_PER_SESSION = 2
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

        # Return availability data 
        with open(CSV_FILE) as file_name:
            file_read = csv.reader(file_name)

            array = list(file_read)
        
        return array


    def generate_data_file(dataFile):
        # Get Supervisor Availability Data
        availability = Data.generate_availability()

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