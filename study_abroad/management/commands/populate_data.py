from typing import Any
from django.core.management.base import BaseCommand
from study_abroad.models import Academics

universities_data = [
    {
        "university_id": 186131,
        "accredation": "Middle States Commission on Higher Education",
        "website": "https://www.princeton.edu",
        "language": "English",
        "acceptance_rate": 0.04,
        "tution_fee": 59810,
        "scholarship": True,
        "application_deadline": "2025-01-01",
        "entrance_exam_unive": False,
        "entrance_exams": "English Proficiency Test (for non-native speakers)",
        "mode_of_study": "On-campus",
        "campus_size": "600 acres",
        "no_of_programs_offered": 36,
        "intl_student_percentage": 12,
        "campus_facilities": "Housing, dining, libraries, research centers, athletic facilities",
        "ranking": 22
    },
    {
        "university_id": 166683,
        "accredation": "New England Commission of Higher Education",
        "website": "https://mitadmissions.org",
        "language": "English",
        "acceptance_rate": 0.04,
        "tution_fee": 59750,
        "scholarship": True,
        "application_deadline": "2025-01-05",
        "entrance_exam_unive": True,
        "entrance_exams": "SAT, ACT, English Proficiency Test",
        "mode_of_study": "On-campus",
        "campus_size": "168 acres",
        "no_of_programs_offered": 50,
        "intl_student_percentage": 10,
        "campus_facilities": "Housing, dining, libraries, labs, sports facilities",
        "ranking": 2
    },
    {
        "university_id": 166027,
        "accredation": "New England Commission of Higher Education",
        "website": "https://www.harvard.edu",
        "language": "English",
        "acceptance_rate": 0.04,
        "tution_fee": 59076,
        "scholarship": True,
        "application_deadline": "2025-01-01",
        "entrance_exam_unive": False,
        "entrance_exams": "English Proficiency Test (for non-native speakers)",
        "mode_of_study": "On-campus",
        "campus_size": "209 acres",
        "no_of_programs_offered": 50,
        "intl_student_percentage": 15,
        "campus_facilities": "Housing, dining, libraries, research centers, athletic facilities",
        "ranking": 4
    },
    {
        "university_id": 243744,
        "accredation": "WASC Senior College and University Commission",
        "website": "https://www.stanford.edu",
        "language": "English",
        "acceptance_rate": 0.04,
        "tution_fee": 62484,
        "scholarship": True,
        "application_deadline": "2025-01-02",
        "entrance_exam_unive": False,
        "entrance_exams": "English Proficiency Test (for non-native speakers)",
        "mode_of_study": "On-campus",
        "campus_size": "8,180 acres",
        "no_of_programs_offered": 67,
        "intl_student_percentage": 12,
        "campus_facilities": "Housing, dining, libraries, research centers, athletic facilities",
        "ranking": 6
    },
    {
        "university_id": 130794,
        "accredation": "New England Commission of Higher Education",
        "website": "https://www.yale.edu",
        "language": "English",
        "acceptance_rate": 0.05,
        "tution_fee": 64700,
        "scholarship": True,
        "application_deadline": "2025-01-02",
        "entrance_exam_unive": False,
        "entrance_exams": "English Proficiency Test (for non-native speakers)",
        "mode_of_study": "On-campus",
        "campus_size": "373 acres",
        "no_of_programs_offered": 60,
        "intl_student_percentage": 11,
        "campus_facilities": "Housing, dining, libraries, research centers, athletic facilities",
        "ranking": 23
    },
    {
        "university_id": 144050,
        "accredation": "Higher Learning Commission",
        "website": "https://www.uchicago.edu",
        "language": "English",
        "acceptance_rate": 0.06,
        "tution_fee": 66939,
        "scholarship": True,
        "application_deadline": "2025-01-03",
        "entrance_exam_unive": False,
        "entrance_exams": "English Proficiency Test (for non-native speakers)",
        "mode_of_study": "On-campus",
        "campus_size": "217 acres",
        "no_of_programs_offered": 60,
        "intl_student_percentage": 12,
        "campus_facilities": "Housing, dining, libraries, research centers, athletic facilities",
        "ranking": 21
    },
    {
        "university_id": 162928,
        "accredation": "Middle States Commission on Higher Education",
        "website": "https://www.jhu.edu",
        "language": "English",
        "acceptance_rate": 0.08,
        "tution_fee": 63340,
        "scholarship": True,
        "application_deadline": "2025-01-02",
        "entrance_exam_unive": False,
        "entrance_exams": "English Proficiency Test (for non-native speakers)",
        "mode_of_study": "On-campus",
        "campus_size": "140 acres",
        "no_of_programs_offered": 50,
        "intl_student_percentage": 15,
        "campus_facilities": "Housing, dining, libraries, research centers, athletic facilities",
        "ranking": 16
    },
    {
        "university_id": 215062,
        "accredation": "Middle States Commission on Higher Education",
        "website": "https://www.upenn.edu",
        "language": "English",
        "acceptance_rate": 0.06,
        "tution_fee": 66104,
        "scholarship": True,
        "application_deadline": "2025-01-05",
        "entrance_exam_unive": False,
        "entrance_exams": "English Proficiency Test (for non-native speakers)",
        "mode_of_study": "On-campus",
        "campus_size": "299 acres",
        "no_of_programs_offered": 90,
        "intl_student_percentage": 14,
        "campus_facilities": "Housing, dining, libraries, research centers, athletic facilities",
        "ranking": 11
    }
]

class Command(BaseCommand):
    help = "Inserts university data into the database"

    def handle(self, *args: Any, **options: Any) -> None:
        for university_data in universities_data:
            Academics.objects.create(
                university_id=university_data["university_id"],
                accredation=university_data["accredation"],
                website=university_data["website"],
                language=university_data["language"],
                acceptance_rate=university_data["acceptance_rate"],
                tution_fee=university_data["tution_fee"],
                scholarship=university_data["scholarship"],
                application_deadline=university_data["application_deadline"],
                entrance_exam_unive=university_data["entrance_exam_unive"],
                entrance_exams=university_data["entrance_exams"],
                mode_of_study=university_data["mode_of_study"],
                campus_size=university_data["campus_size"],
                no_of_programs_offered=university_data["no_of_programs_offered"],
                intl_student_percentage=university_data["intl_student_percentage"],
                campus_facilities=university_data["campus_facilities"],
                ranking=university_data["ranking"]
            )

        self.stdout.write(self.style.SUCCESS(" Data inserted successfully!"))
