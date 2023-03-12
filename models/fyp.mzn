% Parameters
int: students;
int: supervisors;

int: max_students_per_session;
int: max_students_per_supervisor;
int: min_supervisors_per_session;
int: max_supervisors_per_session;

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


% Predicates
predicate count_geq(array [$X] of var int: x,
                    int: y, 
                    int: c);


% Constraints %
constraint forall (t in Timeslots, s in Sessions) (
    % Set max Students per Session
    card(session_students[t,s]) <= max_students_per_session /\
    % Set min Supervisors per Session
    card(session_supervisors[t,s]) >= min_supervisors_per_session /\
    % Set max Supervisors per Session
    card(session_supervisors[t,s]) <= max_supervisors_per_session /\
    
    % Student must be in same Session as Supervisor
    forall(st in session_students[t,s]) (
        student_supervisor[st] in session_supervisors[t,s] 
    )
 ); 
 
% Set max Students per Supervisor
constraint forall(s in Supervisors) (
    count_geq(student_supervisor, s, max_students_per_supervisor)
);


constraint forall(t in Timeslots, s1,s2 in Sessions where s1 != s2) (
    % Supervisor can't be in Concurrent Sessions
    card(session_supervisors[t,s1] intersect session_supervisors[t,s2]) = 0 /\
    % Students can't be in Concurrent Sessions
    card(session_students[t,s1] intersect session_students[t,s2]) = 0
);

% Students can't be in multiple timeslots
constraint forall(t1,t2 in Timeslots where t1 != t2, s in Sessions) (
    card(session_students[t2,s] intersect session_students[t1,s]) = 0
);

% Students only appear once
constraint forall(t1, t2 in Timeslots where t1!=t2, s1, s2 in Sessions where s1!=s2) (
    card(session_students[t1,s1] intersect session_students[t2,s2]) = 0
);



% Check Supervisor Availability
constraint forall(s in Supervisors, t in Timeslots) (
   (availability[s,t] = false) -> forall(ss in Sessions) (
       card(session_supervisors[t,ss] intersect {s}) = 0
    )
);


% Solve
solve satisfy;


% Output
output ["Timeslot/Session Assignments:\n"];
output [ "[T\(t)/S\(s)]:" ++ "\n" ++
        "Supervisors -> " ++ show(session_supervisors[t,s]) ++ "\n" ++
        "Students -> " ++ show(session_students[t,s])  ++ "\n\n"
        | t in Timeslots, s in Sessions];
        
output ["Student Supervisors:\n"];        
output [ "Student[\(st)] -> " ++ show(student_supervisor[st]) ++ "\n"
       | st in Students];