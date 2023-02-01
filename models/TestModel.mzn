%Parameters
int: students;
int: numTimes;
int: numRooms;
int: maxGroupSize;
int: maxSuper; %max Students to a Supervisor

set of int: timeSlots = 1..numTimes;
set of int: rooms = 1..numRooms;


%Decision Variables
array2d(1..numTimes,1..numRooms) of int: timeVenuePairs; %might not be needed?

output ["numStudents: \(students)\n",
        "maxGroupSize: \(maxGroupSize)\n",
        "timeSlots: \(numTimes)\n",
        "maxS: \(rooms)"];