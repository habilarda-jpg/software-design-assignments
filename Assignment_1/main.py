import sys
from datetime import date

from models.academic_term import AcademicTerm
from models.course import Course
from models.course_prerequisite import CoursePrerequisite
from models.department import Department
from models.enums import (
    CourseType,
    DegreeLevel,
    Gender,
    InstructorTitle,
    PrerequisiteType,
    ProgramCourseType,
    Semester,
    StudentStatus,
)
from models.faculty import Faculty
from models.instructor import Instructor
from models.program import Program
from models.program_course import ProgramCourse
from models.student import Student


def print_header(title: str) -> None:
    print(f"\n=== {title} ===")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")

    faculty = Faculty(
        code="MUH",
        name="Mühendislik Fakültesi",
        phone="0212 000 00 00",
        email="muhendislik@universite.edu.tr",
    )

    department = Department(
        code="BLM",
        name="Bilgisayar Mühendisliği",
        faculty=faculty,
        phone="0212 000 00 01",
        email="bilgisayar@universite.edu.tr",
    )

    dean = Instructor(
        employee_no="P0001",
        national_id="11111111110",
        first_name="Ayşe",
        last_name="Yılmaz",
        email="ayse.yilmaz@universite.edu.tr",
        department=department,
        title=InstructorTitle.PROFESSOR,
        specialization="Yapay Zeka",
        hire_date=date(2005, 9, 1),
    )

    head_instructor = Instructor(
        employee_no="P0002",
        national_id="22222222220",
        first_name="Mehmet",
        last_name="Demir",
        email="mehmet.demir@universite.edu.tr",
        department=department,
        title=InstructorTitle.ASSOCIATE_PROFESSOR,
        specialization="Veri Yapıları",
        hire_date=date(2012, 2, 15),
    )

    faculty.dean = dean
    department.head_instructor = head_instructor

    program = Program(
        code="BLM-LIS",
        name="Bilgisayar Mühendisliği Lisans Programı",
        department=department,
        degree_level=DegreeLevel.BACHELOR,
        total_credits=240,
        duration_years=4,
        language="TR",
    )

    intro_course = Course(
        code="BLM101",
        name="Programlamaya Giriş",
        department=department,
        credits=6,
        theory_hours=3,
        lab_hours=2,
        course_type=CourseType.COMPULSORY,
        language="TR",
        description="Temel programlama kavramları",
    )

    data_structures_course = Course(
        code="BLM201",
        name="Veri Yapıları",
        department=department,
        credits=6,
        theory_hours=3,
        lab_hours=2,
        course_type=CourseType.COMPULSORY,
        language="TR",
        description="Temel veri yapıları ve algoritmalar",
    )

    prerequisite = CoursePrerequisite(
        course=data_structures_course,
        prerequisite_course=intro_course,
        type=PrerequisiteType.REQUIRED,
        min_grade="DD",
    )

    program_course = ProgramCourse(
        program=program,
        course=intro_course,
        semester_order=1,
        course_type=ProgramCourseType.COMPULSORY,
    )

    term = AcademicTerm(
        code="2024-1",
        name="2024-2025 Güz Dönemi",
        academic_year="2024-2025",
        semester=Semester.FALL,
        start_date=date(2024, 9, 30),
        end_date=date(2025, 1, 17),
        registration_start=date(2024, 9, 16),
        registration_end=date(2024, 9, 27),
        add_drop_end=date(2024, 10, 11),
    )

    print_header("Faculty")
    print(faculty)

    print_header("Department")
    print(department)

    print_header("Instructor")
    print(dean)
    print(head_instructor)

    print_header("Program")
    print(program)

    print_header("Course")
    print(intro_course)
    print(data_structures_course)

    print_header("CoursePrerequisite")
    print(prerequisite)

    print_header("ProgramCourse")
    print(program_course)

    print_header("AcademicTerm")
    print(term)

    students: list[Student] = []

    student = Student(
        student_no="240000001",
        national_id="12345678901",
        first_name="Arda",
        last_name="Koyunlu",
        birth_date=date(2006, 1, 1),
        gender=Gender.MALE,
        email="240000001@st.universite.edu.tr",
        phone="0555 000 00 00",
        address="İstanbul",
        program=program,
        enrollment_year=2024,
        class_year=1,
        status=StudentStatus.ACTIVE,
    )
    students.append(student)

    print_header("Student")
    print("Kayıtlı öğrenciler:")
    for registered_student in students:
        print(registered_student)


if __name__ == "__main__":
    main()
