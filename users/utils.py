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
def serializer_create(serializer_cls, **kwargs):
    serializer = serializer_cls(**kwargs)
    serializer.is_valid(raise_exception = True)
    serializer.save()
    return serializer.data