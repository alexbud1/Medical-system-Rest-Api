import datetime
import pytz


SPECIALIZATION_CHOICES =(
    ("Allergist/Immunologist", "Allergist/Immunologist"),
    ("Anesthesiologist", "Anesthesiologist"),
    ("Cardiologist", "Cardiologist"),
    ("Colon and Rectal Surgeon", "Colon and Rectal Surgeon"),
    ("Critical Care Medicine Specialist", "Critical Care Medicine Specialist"),
    ("Dermatologist", "Dermatologist"),
    ("Endocrinologist", "Endocrinologist"),
    ("Emergency Medicine Specialist", "Emergency Medicine Specialist"),
    ("Family Physician", "Family Physician"),
    ("Gastroenterologist", "Gastroenterologist"),
    ("Geriatric Medicine Specialist", "Geriatric Medicine Specialist"),
    ("Hematologist", "Hematologist"),
    ("Hospice and Palliative Medicine Specialist", "Hospice and Palliative Medicine Specialist"),
    ("Infectious Disease Specialist", "Infectious Disease Specialist"),
    ("Internist", "Internist"),
    ("Medical Geneticist", "Medical Geneticist"),
    ("Nephrologist", "Nephrologist"),
    ("Neurologist", "Neurologist"),
    ("Obstetrician and Gynecologist", "Obstetrician and Gynecologist"),
    ("Oncologist", "Oncologist"),
    ("Ophthalmologist", "Ophthalmologist"),
    ("Osteopath", "Osteopath"),
    ("Otolaryngologist", "Otolaryngologist"),
    ("Pathologist", "Pathologist"),
    ("Pediatrician", "Pediatrician"),
    ("Physiatrist", "Physiatrist"),
    ("Plastic Surgeon", "Plastic Surgeon"),
    ("Podiatrist", "Podiatrist"),
    ("Preventive Medicine Specialist", "Preventive Medicine Specialist"),
    ("Psychiatrist", "Psychiatrist"),
    ("Pulmonologist", "Pulmonologist"),
    ("Radiologist", "Radiologist"),
    ("Rheumatologist", "Rheumatologist"),
    ("Sports Medicine Specialist", "Sports Medicine Specialist"),
    ("General Surgeon", "General Surgeon"),
    ("Urologist", "Urologist"),
)

STAFF_ROLE_CHOICES = (
    ("CallCenter", "Call Center"),
    ("Administrator", "Administrator"),
)

SEX_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)
def serializer_create(serializer_cls, **kwargs):
    serializer = serializer_cls(**kwargs)
    serializer.is_valid(raise_exception = True)
    serializer.save()
    return serializer.data

def check_week(date):
    today = datetime.datetime.now()
    weekday = today.isoweekday()
    weekdays = []
    for i in range(1,8):
        if i <= weekday:
            weekdays.append((today - datetime.timedelta(days=weekday - i)).strftime("%m/%d/%Y"))
        else:
            weekdays.append((today + datetime.timedelta(days=i - weekday)).strftime("%m/%d/%Y"))

    if date in weekdays:
        return True
    else:
        return False

def check_semester(date):
    utc=pytz.UTC
    today = utc.localize(datetime.datetime.now())
    second_semester_start  = utc.localize(datetime.datetime(today.year, 7, 1))
    first_semester_start  = utc.localize(datetime.datetime(today.year, 1, 1))
    if first_semester_start <= today < second_semester_start:
        if first_semester_start <= date < second_semester_start:
            return True
        else:
            return False
    else:
        if date >= second_semester_start and date.year == today.year:
            return True
        else:
            return False

class Statistics():
    def __init__(self, all_clients, boys16, girls, guys, children, disabled):
        self.all_clients = all_clients
        self.boys16 = boys16
        self.girls = girls
        self.guys = guys
        self.children = children
        self.disabled = disabled

    def get_statistics(self):
        statistics = {
                "general_quantity" : self.all_clients,
                "boys1to16" : self.boys16,
                "girls" : self.girls,
                "guys16to18" : self.guys,
                "children0to1" : self.children,
                "disabled" : self.disabled
            }
        return statistics
