% Parameters
int: students;
int: supervisors;

int: max_students_per_session;
int: max_students_per_supervisor;
int: min_supervisors_per_session;

int: timeslots;
int: sessions;

array[Supervisors, Timeslots] of bool: availability;

% Sets
set of int: Students = 1..students;
set of int: Supervisors = 1..supervisors;
set of int: Timeslots = 1..timeslots;
set of int: Sessions = 1..sessions;

% Variables
array[Students] of var Supervisors: student_supervisor;
array[Timeslots, Sessions] of var set of Students: session_students;
array[Timeslots, Sessions] of var set of Supervisors: session_supervisors;


% Constraints
constraint forall (t in Timeslots, s in Sessions) (
    card(session_students[t,s]) <= max_students_per_session /\
    card(session_supervisors[t,s]) >= min_supervisors_per_session /\
    
    forall(st in session_students[t,s]) (
        student_supervisor[st] in session_supervisors[t,s]
    )
 ); 
 
constraint forall(s in Supervisors) (
    count_leq(max_students_per_supervisor, s, student_supervisor)
);

constraint forall(t in Timeslots, s1 in Sessions, s2 in Sessions where s1 < s2) (
    card(session_students[t,s1] intersect session_students[t,s2]) = 0 /\
    card(session_supervisors[t,s1] intersect session_supervisors[t,s2]) = 0
);

constraint forall(s in Supervisors, t in Timeslots) (
    (availability[s,t] = false) -> forall(ss in Sessions) (
        card(session_supervisors[t,ss] intersect {s}) = 0
    )
);


% Solve
solve satisfy;
