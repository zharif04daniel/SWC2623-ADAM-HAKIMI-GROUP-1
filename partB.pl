student(hana, am001).
student(achik, am002).
student(aina, am003).
student(amin, am004).
student(zafran, am005).
student(adam, am006).


module(c101).
module(c102).
module(c103).
module(c104).
module(c105).
module(c106).


enrolled(am001, c101).
enrolled(am001, c102).
enrolled(am001, c103).

enrolled(am002, c101).
enrolled(am002, c102).

enrolled(am003, c101).
enrolled(am003, c102).
enrolled(am003, c103).
enrolled(am003, c104).
enrolled(am003, c105).
enrolled(am003, c106).

enrolled(am004, c101).

enrolled(am005, c101).
enrolled(am005, c102).
enrolled(am005, c103).

enrolled(am006, c101).
enrolled(am006, c102).


prerequisite(c102, c101).
prerequisite(c103, c102).
prerequisite(c104, c101).
prerequisite(c105, c103).
prerequisite(c106, c104).


required_course(c101).
required_course(c102).
required_course(c103).
required_course(c104).
required_course(c105).
required_course(c106).


eligible(StudentID, CourseCode) :-
    module(CourseCode),
    forall(
        prerequisite(CourseCode, PrereqCourse),
        enrolled(StudentID, PrereqCourse)
    ),
    \+ enrolled(StudentID, CourseCode).


recommend_course(StudentID, CourseCode) :-
    eligible(StudentID, CourseCode).


certification_eligible(StudentID) :-
    student(_, StudentID),
    forall(
        required_course(Course),
        enrolled(StudentID, Course)
    ).