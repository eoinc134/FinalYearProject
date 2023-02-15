% Parameters
int: n_students;
int: n_supervisors;
int: n_timeslots;
int: n_rooms;
int: max_presentations_per_time_slot;

% Sets
set of int: Students = 1..n_students;
set of int: Supervisors = 1..n_supervisors;
set of int: TimeSlots = 1..n_timeslots;
set of int: Rooms = 1..n_rooms;

% Arrays
array[Students] of int: supervisor;
array[Supervisors, TimeSlots] of bool: supervisor_available;
array[TimeSlots] of bool: timeslot_available;
array[Students, TimeSlots, Rooms, TimeSlots] of bool: scheduled;
array[TimeSlots] of int: presentations_scheduled_per_timeslot;

% Constraints
constraint forall(s in Students, t in TimeSlots, r in Rooms, d1, d2 in TimeSlots where d1 != d2) (
    scheduled[s, t, r, d1] /\ scheduled[s, t, r, d2] -> false
);

constraint forall(s in Students, t in TimeSlots, r in Rooms) (
    sum([scheduled[s, t, r, d] | d in TimeSlots]) <= 1
);

constraint forall(s in Students, r in Rooms, t in TimeSlots) (
    sum([scheduled[s, t, r, d] | d in TimeSlots]) <= 1
);

constraint forall(s in Students, t in TimeSlots, r in Rooms) (
    supervisor_available[supervisor[s], t] /\ timeslot_available[t] -> scheduled[s,t,r,t]
);

constraint forall(t in TimeSlots) (
    presentations_scheduled_per_timeslot[t] = sum([bool2int(scheduled[s, t, r, t]) | s in Students, r in Rooms])
);

constraint forall(t in TimeSlots) (
    presentations_scheduled_per_timeslot[t] <= max_presentations_per_time_slot
);

% Solve
solve satisfy;

% Output
output [
    if scheduled[s, t, r, d] then
        "Student \(s) presents in room \(r) during timeslot \(t) at day \(d)\n"
    else
        ""
    endif
    | s in Students, t in TimeSlots, r in Rooms, d in TimeSlots
];
