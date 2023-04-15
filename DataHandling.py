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
availability = 0.7
NEW_DATA_FILE = True
CSV_FILE = "./data/availability.csv"

class Data:
    """
    Class to generate and retrieve data for scheduling problem.
    """

    @staticmethod
    def generate_availability():
        """
        Generate availability data for supervisors.
        """
        with open(CSV_FILE, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for i in range(1, NUM_SUPERVISORS + 1):
                row = [random.choices(['true', 'false'], weights=(availability, 1- availability))[0] for j in range(TIMESLOTS)]
                writer.writerow(row)

    @staticmethod
    def get_availability_data():
        """
        Retrieve availability data for supervisors.
        """
        # Generate new availability lists
        if NEW_DATA_FILE:
            Data.generate_availability()

        # Return availability data
        with open(CSV_FILE) as file_name:
            file_read = csv.reader(file_name)
            array = list(file_read)
        return array

    @staticmethod
    def generate_data_file(data_file):
        """
        Generate data file for scheduling problem.
        """
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
        with open(data_file, 'w') as outfile:
            outfile.write("\n".join(dzn.dict2dzn(data)))

    @staticmethod
    def verify_output(result):
        """
        Verify that all students are assigned to a session.
        """
        students = result['session_students']

        # Add up all students in all sessions
        num_students = 0
        for timeslot in students:
            for session in timeslot:
                for student in session:
                    num_students += 1

        # Verify all students assigned a slot
        if num_students != NUM_STUDENTS :
                print(f"Invalid Output: {NUM_STUDENTS - num_students} students missing from assignment")
                return False
        return True
