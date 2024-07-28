--STAGING LAYER
CREATE TABLE stg_lecturer (
    ID INT PRIMARY KEY,
    Nama VARCHAR(255)
);

CREATE TABLE stg_student (
    ID INT PRIMARY KEY,
    Nama VARCHAR(255)
);

CREATE TABLE stg_enrollment (
    ID INT PRIMARY KEY,
    STUDENT_ID INT,
    SCHEDULE_ID INT,
    ACADEMIC_YEAR VARCHAR(9),
    SEMESTER INT,
    ENROLL_DT DATE
);

CREATE TABLE stg_schedule (
    ID INT PRIMARY KEY,
    COURSE_ID INT,
    LECTURER_ID INT,
    START_DT DATE,
    END_DT DATE,
    COURSE_DAYS VARCHAR(50)
);

CREATE TABLE stg_course (
    ID INT PRIMARY KEY,
    NAME VARCHAR(255)
);

CREATE TABLE stg_course_attendance (
    ID INT PRIMARY KEY,
    STUDENT_ID INT,
    SCHEDULE_ID INT,
    ATTEND_DT DATE
);


--DATA INTEGRATION LAYER
CREATE TABLE dim_lecturer (
    LecturerID INT PRIMARY KEY,
    LecturerName VARCHAR(255)
);

CREATE TABLE dim_student (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(255)
);

CREATE TABLE dim_course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(255)
);

CREATE TABLE dim_schedule (
    ScheduleID INT PRIMARY KEY,
    CourseID INT,
    LecturerID INT,
    StartDate DATE,
    EndDate DATE,
    CourseDays VARCHAR(50),
    FOREIGN KEY (CourseID) REFERENCES dim_course(CourseID),
    FOREIGN KEY (LecturerID) REFERENCES dim_lecturer(LecturerID)
);

CREATE TABLE fact_enrollment (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    ScheduleID INT,
    AcademicYear VARCHAR(9),
    Semester INT,
    EnrollDate DATE,
    FOREIGN KEY (StudentID) REFERENCES dim_student(StudentID),
    FOREIGN KEY (ScheduleID) REFERENCES dim_schedule(ScheduleID)
);

CREATE TABLE fact_course_attendance (
    AttendanceID INT PRIMARY KEY,
    StudentID INT,
    ScheduleID INT,
    AttendDate DATE,
    FOREIGN KEY (StudentID) REFERENCES dim_student(StudentID),
    FOREIGN KEY (ScheduleID) REFERENCES dim_schedule(ScheduleID)
);



--PRESENTATION LAYER
CREATE TABLE weekly_attendance (
    SEMESTER_ID INT,
    WEEK_ID INT,
    COURSE_NAME VARCHAR(255),
    ATTENDANCE_PCT FLOAT
);

