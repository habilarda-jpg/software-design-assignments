from enum import Enum


class Gender(Enum):
    MALE = "E"
    FEMALE = "K"


class DegreeLevel(Enum):
    ASSOCIATE = "önlisans"
    BACHELOR = "lisans"
    MASTER = "yüksek_lisans"
    DOCTORATE = "doktora"


class StudentStatus(Enum):
    ACTIVE = "aktif"
    GRADUATED = "mezun"
    SUSPENDED = "askı"
    WITHDRAWN = "ayrıldı"


class InstructorTitle(Enum):
    LECTURER = "öğr.gör."
    DOCTOR = "dr."
    ASSISTANT_PROFESSOR = "dr.öğr.üyesi"
    ASSOCIATE_PROFESSOR = "doç.dr."
    PROFESSOR = "prof.dr."


class CourseType(Enum):
    COMPULSORY = "zorunlu"
    ELECTIVE = "seçmeli"
    NON_DEPARTMENTAL_ELECTIVE = "ASD"


class ProgramCourseType(Enum):
    COMPULSORY = "zorunlu"
    ELECTIVE = "seçmeli"


class Semester(Enum):
    FALL = "güz"
    SPRING = "bahar"
    SUMMER = "yaz"


class PrerequisiteType(Enum):
    REQUIRED = "zorunlu"
    RECOMMENDED = "önerilen"
