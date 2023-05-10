from django.db import models
from django import forms
from django.forms import MultipleChoiceField
from django.forms.models import ModelMultipleChoiceField
# Create your models here.

class Ministry(models.Model):
    ministry_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ministry_name
    
class Department(models.Model):
    department_name = models.CharField(max_length=255)
    ministry = models.ForeignKey(Ministry,null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.department_name
    
class PrimaryGroup(models.Model):
    primary_group_name = models.CharField(max_length=255)

    def __str__(self):
        return self.primary_group_name
    
class Category(models.Model):
    primary_group = models.ForeignKey(PrimaryGroup, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)
    is_central_sector = models.BooleanField(default=False)
    is_centrally_sponsored = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name

class MaritalStatus(models.Model):

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ]

    marital_status = models.CharField(max_length=100, choices=MARITAL_STATUS_CHOICES, unique= True)

    def __str__(self):
        return self.marital_status

class Disability(models.Model):

    DISABILITY_CHOICES = [
        ('Full', 'Full'),
        ('Partial', 'Partial'),
        ('None', 'None'),
    ]

    disability = models.CharField(
        max_length=10,
        choices=DISABILITY_CHOICES,
        default='None',
    )

    def __str__(self):
        return self.disability

class Education(models.Model):

    EDUCATION_CHOICES = [
        ('Diploma', 'Diploma'),
        ("Bachelor's", "Bachelor's"),
        ('Masters', 'Masters'),
        ('PHD', 'PHD'),
        ('High School', 'High School'),
        ('Middle School', 'Middle School'),
    ]

    education = models.CharField(
        max_length=100,
        choices=EDUCATION_CHOICES,
    )

    def __str__(self):
        return self.education

class Caste(models.Model):

    CASTE_CHOICES = [
        ('General', 'General'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
        ('EWS', 'EWS'),
    ]
    # CASTE_CHOICES = [
    #     ('General', 'General'),
    #     ('SC', 'SC'),
    #     ('Scheduled Tribe', 'Scheduled Tribe'),
    #     ('Other Backward Class', 'Other Backward Class'),
    #     ('Economically Weaker Section', 'Economically Weaker Section'),
    # ]

    caste = models.CharField(
        max_length=100,
        choices=CASTE_CHOICES,
    )
    def __str__(self):
        return self.caste

class Gender(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    def __str__(self):
        return self.gender


    
class Occupation(models.Model):

    OCCUPATION_CHOICES = [
        ('Unemployed', 'Unemployed'),
        ('Farmer', 'Farmer'),
        ('Fisherman', 'Fisherman'),
    ]

    occupation = models.CharField(max_length=100,choices=OCCUPATION_CHOICES)
    def __str__(self):
        return self.occupation


class State(models.Model):
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

    
    state_name = models.CharField(max_length=200, choices=STATE_CHOICES)
    
    def __str__(self):
        return self.state_name
    
class District(models.Model):
    
    district_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.district_name
    
class AgeGroup(models.Model):
    
    AGE_GROUP_CHOICES= [
        ('0-6','0-6'),
        ('7-15','7-15'),
        ('16-30','16-30'),
        ('31-58','31-58'),
        ('58-200','58-200'),
    ]
    age_group = models.CharField(max_length=200,choices=AGE_GROUP_CHOICES)
    
    def __str__(self):
        return self.age_group
    
class IncomeGroup(models.Model):
    
    INCOME_GROUP_CHOICES= [
        ('0-100000','0-100000'),
        ('100000-500000','100000-500000'),
        ('500000-1000000','500000-1000000'),
        ('1000000-2500000','1000000-2500000'),
        ('2500000-4500000','2500000-4500000'),
        ('4500000-100000000','4500000-100000000'),
    ]
    income_group = models.CharField(max_length=200,choices=INCOME_GROUP_CHOICES)
    
    def __str__(self):
        return self.income_group
        
class Income(models.Model):
    
    district_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.district_name
    
class Beneficiary(models.Model):
    
    beneficiary_name = models.CharField(max_length=200)
    primary_group = models.CharField(max_length=200,null=True, blank=True)
    is_individual = models.BooleanField(default=False)
    is_non_individual = models.BooleanField(default=False)

    def __str__(self):
        return self.beneficiary_name
    
class Scheme(models.Model):

    SCHEME_TYPE_CHOICES = [
        ('Individual','Individual'),
        ('Non-Individual','Non-Individual')
    ]
    ministry = models.ForeignKey(Ministry, on_delete=models.SET_NULL,blank = True, null =True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,blank = True, null =True)
    scheme_name  = models.CharField(max_length=255)
    # min_age = models.PositiveIntegerField(null=True, blank= True)
    # max_age = models.PositiveIntegerField(null=True, blank= True)
    income_groups_applicable = models.ManyToManyField(IncomeGroup, null=True, blank= True)
    age_groups_applicable = models.ManyToManyField(AgeGroup, null=True, blank= True)
    genders_applicable = models.ManyToManyField(Gender, null=True, blank= True)
    marital_status_applicable = models.ManyToManyField(MaritalStatus, null=True, blank= True)
    disabilities_applicable = models.ManyToManyField(Disability, null=True, blank= True)
    states_applicable = models.ManyToManyField(State, null=True, blank= True)
    districts_applicable = models.ManyToManyField(District, null=True, blank= True)
    is_rural = models.BooleanField(default=False)
    is_urban = models.BooleanField(default=False)
    education_applicable = models.ManyToManyField(Education, null=True, blank= True)
    occupation_applicable = models.ManyToManyField(Occupation, null=True, blank= True)
    beneficiaries_applicable = models.ManyToManyField(Beneficiary, null=True, blank= True)
    # min_income = models.PositiveIntegerField( null=True, blank= True)
    # max_income = models.PositiveIntegerField( null=True, blank= True)
    castes_applicable = models.ManyToManyField(Caste, null=True, blank= True)
    sector = models.CharField(max_length=100, null=True, blank= True)
    categories = models.ManyToManyField(Category, null=True, blank= True)
    is_central_sector = models.BooleanField(default=False)
    is_centrally_sponsored = models.BooleanField(default=False)
    # scheme_type  = models.CharField(max_length=50,choices=SCHEME_TYPE_CHOICES, default='Individual')
    is_individual = models.BooleanField(default=False)
    is_non_individual = models.BooleanField(default=False)
    link = models.URLField(blank=True,null=True)
    budget  = models.CharField(max_length=100,null = True, blank = True)
    
    def __str__(self):
        return self.scheme_name
    

