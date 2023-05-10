from .models import *

def create_marital_status():

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]
    for status in MARITAL_STATUS_CHOICES:
        MaritalStatus.objects.get_or_create(marital_status=status[0])
        
def create_disability():

    DISABILITY_CHOICES = [
        ('Full', 'Full'),
        ('Partial', 'Partial'),
        ('None', 'None'),
    ]

    for disability in DISABILITY_CHOICES:
        Disability.objects.get_or_create(disability=disability[0])
        
def create_education():

    EDUCATION_CHOICES = [
        ('Diploma', 'Diploma'),
        ("Bachelor's", "Bachelor's"),
        ('Masters', 'Masters'),
        ('PHD', 'PHD'),
        ('High School', 'High School'),
        ('Middle School', 'Middle School'),
    ]
    for education in EDUCATION_CHOICES:
        Education.objects.get_or_create(education=education[0])
        
def create_castes():

    CASTE_CHOICES = [
        ('General', 'General'),
        ('Scheduled Caste', 'Scheduled Caste'),
        ('Scheduled Tribe', 'Scheduled Tribe'),
        ('Other Backward Class', 'Other Backward Class'),
        ('Economically Weaker Section', 'Economically Weaker Section'),
    ]

    for caste in CASTE_CHOICES:
        Caste.objects.get_or_create(caste=caste[0])
        
def create_genders():

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    for gender in GENDER_CHOICES:
        Gender.objects.get_or_create(gender=gender[0])
        
def create_age_groups():

    AGE_GROUP_CHOICES= [
        ('0-6','0-6'),
        ('7-15','7-15'),
        ('16-30','16-30'),
        ('31-58','31-58'),
        ('58-200','58-200'),
    ]
    for age_group in AGE_GROUP_CHOICES:
        AgeGroup.objects.get_or_create(age_group=age_group[0])
        
def create_income_groups():

    INCOME_GROUP_CHOICES= [
        ('0-100000','0-100000'),
        ('100000-500000','100000-500000'),
        ('500000-1000000','500000-1000000'),
        ('1000000-2500000','1000000-2500000'),
        ('2500000-4500000','2500000-4500000'),
        ('4500000-100000000','4500000-100000000'),
    ]
    for income_group in INCOME_GROUP_CHOICES:
        IncomeGroup.objects.get_or_create(income_group=income_group[0])
        
def create_occupations():

    OCCUPATION_CHOICES = [
        ('Unemployed', 'Unemployed'),
        ('Farmer', 'Farmer'),
        ('Fisherman', 'Fisherman'),
    ]
    for occupation in OCCUPATION_CHOICES:
        Occupation.objects.get_or_create(occupation=occupation[0])
        
def create_states():

    STATE_CHOICES = [
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Ladakh', 'Ladakh'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ]

    for state in STATE_CHOICES:
        State.objects.get_or_create(state_name=state[0])