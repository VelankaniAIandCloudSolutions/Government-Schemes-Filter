from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.db.models import Q
import pandas as pd
from django.db import IntegrityError
import locale
from decimal import Decimal

# def my_view(request):
#     print(request)

#     data = {
#         'message': 'Hello, Wix!',
#         'number': 42,
#         'is_true': True,
#     }
#     return JsonResponse(data)

@csrf_exempt
def filter_wix_data(request):
    if request.method =='POST':
        json_data = JSONParser().parse(request)

        # income_ranges = {
        #     "Less than 1 Lakh": (0, 100000),
        #     "1 to 5 Lakhs": (100000, 500000),
        #     "5 to 10 Lakhs": (500000, 1000000),
        #     "10 to 25 Lakhs": (1000000, 2500000),
        #     "25 to 45 Lakhs": (2500000, 4500000),
        #     "45 Lakhs and above": (4500000, 100000000000),
        #     "":(0,100000000000)
        # }

        # income_range = json_data.get('income')
        # if income_range=='':
        #     lower_income, upper_income = 0,100000000
        # else:
        #     lower_income, upper_income = income_range.split("-")
        # lower_income = int(lower_income)
        # upper_income = int(upper_income)
        # q_income_filter = Q(min_income__gte=lower_income, min_income__lte=upper_income) & Q(max_income__gte=lower_income, max_income__lte=upper_income)

        # age_range = json_data.get('age')
        # if age_range=='':
        #     lower, upper = 0,120
        # else:
        #     lower, upper = age_range.split("-")
        # lower = int(lower)
        # upper = int(upper)
        # q_age_filter = Q(min_age__gte=lower, min_age__lte=upper) & Q(max_age__gte=lower, max_age__lte=upper)


        # q_gender_filters = Q()
        # gender = json_data.get('gender')
        # q_gender_filters |= Q(genders_applicable__gender=gender)

        # q_disability_filters = Q()
        # disability = json_data.get('disabili')
        # q_disability_filters |= Q(disabilities_applicable__disability=disability)

        # q_marital_status_filters = Q()
        # marital_status= json_data.get('marital_status')
        # q_marital_status_filters |= Q(marital_status_applicable__marital_status=marital_status)

        if json_data.get('scheme_type').strip()=='Individual':
            is_individual  = True
            is_non_individual = False
        else:
            is_individual = False
            is_non_individual = True
        
        schemes_of_one_type   = Scheme.objects.filter(Q(is_individual = is_individual, is_non_individual = is_non_individual)).distinct().order_by('scheme_name')

        perfect_match_schemes  = Scheme.objects.filter( 
                                                        Q(is_individual = is_individual, is_non_individual = is_non_individual) &
                                                        Q(beneficiaries_applicable__beneficiary_name=str(json_data.get('beneficiary')).strip()) & 
                                                        Q(beneficiaries_applicable__primary_group=str(json_data.get('primary_group')).strip()) & 
                                                        Q(castes_applicable__caste=str(json_data.get('caste')).strip()) & 
                                                        Q(genders_applicable__gender=str(json_data.get('gender')).strip()) & 
                                                        Q(marital_status_applicable__marital_status=str(json_data.get('marital_status')).strip()) 
                                                    ).distinct().order_by('scheme_name')
        
        close_match_schemes  = Scheme.objects.filter(Q(is_individual = is_individual, is_non_individual = is_non_individual) &
                                                    Q(beneficiaries_applicable__beneficiary_name=str(json_data.get('beneficiary')).strip()) | 
                                                    Q(beneficiaries_applicable__primary_group=str(json_data.get('primary_group')).strip()) | 
                                                    Q(castes_applicable__caste=str(json_data.get('caste')).strip()) | 
                                                    Q(genders_applicable__gender=str(json_data.get('gender')).strip()) | 
                                                    Q(marital_status_applicable__marital_status=str(json_data.get('marital_status')).strip()) 
                                                    ).distinct().order_by('scheme_name')
        
        schemes_of_one_type_serializer = SchemeSeraizlier(schemes_of_one_type,many = True)
        perfect_match_schemes_serializer = SchemeSeraizlier(perfect_match_schemes,many = True)
        close_match_schemes_serializer = SchemeSeraizlier(close_match_schemes,many = True)
        departments_serializer = DepartmentSeraizlier(Department.objects.all(),many = True)
        ministrires_serializer = MinistrySerializer(Ministry.objects.all(),many = True)

        # print(close_match_schemes_serializer.data)

        data = {
            'schemes_of_one_type': schemes_of_one_type_serializer.data,
            'perfect_match_schemes': perfect_match_schemes_serializer.data,
            'close_match_schemes': close_match_schemes_serializer.data,
            'departments': departments_serializer.data,
            'ministries': ministrires_serializer.data,
        }
        # data = {
        #     'schemes_of_one_type': 'schemes_of_one_type_serializer.data',

        # }
        return JsonResponse(data)
    
    if request.method  == "GET":

        data = {
            'schemes_of_one_type': 'hahhahah',
        }
        return JsonResponse(data)
    

@csrf_exempt
def get_beneficiaries(request):
    if request.method =='GET':

        unique_primary_groups_qs = Beneficiary.objects.filter(
            Q(primary_group__isnull=False) & ~Q(primary_group='')
        ).values('primary_group').distinct()

        unique_primary_groups_list = [dict(primary_group=item[0]) for item in unique_primary_groups_qs.values_list('primary_group')]

        print(unique_primary_groups_list)

        beneficiaries  = Beneficiary.objects.all()
        beneficiaries_serializer  = BeneficiarySerializer(beneficiaries, many = True)
        data = {
            'beneficiaries': beneficiaries_serializer.data,
            'primary_groups': unique_primary_groups_list,
        }
        return JsonResponse(data)
    



def import_beneficiaries(request):
    if request.method == "GET":
        
        df = pd.read_excel('media/beneficiaries.xlsx', sheet_name='beneficiary_list',header=1)
        # df = df.head(10)
        print(df.columns.tolist())

        for index, row in df.iterrows():
            print(row['Primary Group'])
            


            if pd.isnull(row['Category Name']) or row['Category Name'] == '':
                print(f"Row {index}:Category Name is blank")
            else:

                if str(row['INDUVIDUAL']) == 'Y':
                    is_individual = True
                else:
                    is_individual = False

                if str(row['NON-INDUVIDUAL']) == 'Y':
                    is_non_individual = True
                else:
                    is_non_individual = False

                beneficiary, created = Beneficiary.objects.update_or_create(beneficiary_name = row['Category Name'],
                                                                            primary_group = row['Primary Group'],
                                                                            is_individual = is_individual,
                                                                            is_non_individual = is_non_individual,
                                                                            )
        data = {
            'beneficiaries': 'imported',
        }
        return JsonResponse(data)  

def import_schemes(request):
    if request.method == "GET":
        # filtered_df = pd.read_excel('media/Schemes Consolidated.xlsx',sheet_name='Centrally Sponsored Schemes',header=0)
        filtered_df = pd.read_excel('media/Schemes Consolidated.xlsx',sheet_name='Centra Sector Schemes',header=0)

        beneficiary_names  = Beneficiary.objects.all().values_list('beneficiary_name', flat=True)
        dept_no = 0
        min_no = 0
        # columns_list = filtered_df.columns.tolist()
        # print(columns_list)
        for index, row in filtered_df.iterrows():
            department = None
            ministry = None

            if pd.isnull(row['Ministry']) or row['Ministry'] == '':
                min_no+=1
                print(f"Row {index}: Name of Ministry is blank")
            else:
                ministry, created = Ministry.objects.update_or_create(ministry_name = row['Ministry'])
                    
            if pd.isnull(row['Department']) or row['Department'] == '':
                dept_no+=1
                print(f"Row {index}: Department is blank")
            else:
                department, created = Department.objects.update_or_create(department_name = row['Department'])

            if pd.isnull(row['Name of the Scheme']) or row['Name of the Scheme'] == '':
                print(f"Row {index}: Name of Scheme is blank")
            else:
                if str(row['Individual']) == 'Y':
                    is_individual = True
                else:
                    is_individual = False
                    
                if str(row['Non-Individual']) == 'Y':
                    is_non_individual = True
                else:
                    is_non_individual = False
                
                if str(row['TOTAL']) != '' or str(row['TOTAL']) != '-' :
                    budget  = str(row['TOTAL'])
                else:
                    budget = ''

                scheme, created = Scheme.objects.update_or_create(
                                                                    scheme_name = row['Name of the Scheme'],
                                                                    department = department,
                                                                    ministry = ministry,
                                                                    is_individual = is_individual,
                                                                    is_non_individual = is_non_individual,
                                                                    defaults={
                                                                        'budget':budget
                                                                    }
                                                                )
                
                if pd.isnull(row['Weblink']) or row['Weblink'] == '':
                    print(f"Row {index}: Name of Web link is blank")
                else:
                    scheme.link = row['Weblink']

                for column_name in filtered_df.columns:
                    if column_name in beneficiary_names:
                        beneficiary = Beneficiary.objects.get(beneficiary_name = column_name)
                        if row[column_name]=='Y':
                            try:
                                scheme.beneficiaries_applicable.add(beneficiary)
                            except IntegrityError:
                                pass

                if(pd.isnull(row['Gender']) or row['Gender'] == ''):
                    print(f"Row {index}: Name of Gender is blank")
                else:
                    gender  = Gender.objects.get(gender = row['Gender'])
                    try:
                        scheme.genders_applicable.add(gender)
                    except IntegrityError:
                        pass
                
                if(pd.isnull(row['Marital Status']) or row['Marital Status'] == ''):
                    print(f"Row {index}: Marital Status is blank")
                else:
                    if row['Marital Status']== 'Widow':
                        marital_status = 'Widowed'
                    marital_status  = MaritalStatus.objects.get(marital_status = marital_status)
                    try:
                        scheme.marital_status_applicable.add(marital_status)
                    except IntegrityError:
                        pass

                if(pd.isnull(row['Caste']) or row['Caste'] == ''):
                    caste = Caste.objects.get(caste= 'General')
                    scheme.castes_applicable.add(caste)
                    print(f"Row {index}: Caste is blank")
                else:
                    castes_list = row['Caste'].split(",")

                    for caste in castes_list:
                        caste  = Caste.objects.get(caste = caste)
                        try:
                            scheme.castes_applicable.add(caste)
                        except IntegrityError:
                            pass

                scheme.save()
        data = {
            'ministry_missing': min_no ,
            'dept_missing': dept_no,
        }
        return JsonResponse(data)  

def format_budget(request):
    if request.method == "GET":
        for scheme in Scheme.objects.all():
            if scheme.budget is None or not scheme.budget.strip() or scheme.budget == '-':
                continue
            else:
                # Set the appropriate locale for your region
                locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
                # Convert the input string to a Decimal number with two decimal points
                input_decimal = Decimal(scheme.budget.strip()).quantize(Decimal('0.01'))
                # Format the Decimal number with commas for thousands and lakhs
                formatted_decimal = locale.format_string('%.2f', input_decimal, grouping=True)
                
                scheme.budget  = formatted_decimal
                scheme.save()

        return JsonResponse({'okay':'okay'})

def import_departments(request):
    if request.method == "GET":

        filtered_df = pd.read_excel('media/Schemes Consolidated.xlsx',sheet_name='Ministry  Departments',header=0)

        for index, row in filtered_df.iterrows():
            print(row)            
            if pd.isnull(row['Name of Ministry']) or row['Name of Ministry'] == '':
                print(f"Row {index}: Name of Ministry is blank")
            else:
                # ministry, created = Ministry.objects.update_or_create(ministry_name = row['Name of Ministry'])

                # if created:
                #     print('Created Min')
                # ministry = Ministry.objects.get(ministry_name = row['Name of Ministry'])
                if row['Name of Department']==row['Name of Ministry']:
                    continue
                # print(Ministry.objects.filter(ministry_name = row['Name of Ministry']).count())

                if(Ministry.objects.filter(ministry_name__iexact = row['Name of Ministry'].lower()).count()>1):
                    ministry= Ministry.objects.filter(ministry_name__iexact = row['Name of Ministry'].lower())[0]
                else:
                    ministry,created  = Ministry.objects.get_or_create(ministry_name__iexact=row['Name of Ministry'].lower())
                if created:
                    print('created min')

                if pd.isnull(row['Name of Department']) or row['Name of Department'] == '':
                    print(f"Row {index}: Department is blank")
                else:
                    if(Department.objects.filter(department_name = row['Name of Department']).count()>1):
                        department = Department.objects.filter(department_name = row['Name of Department'])[0]
                    else:
                        department,created = Department.objects.get_or_create(department_name = row['Name of Department'])
                    
                    if created:
                        print('dept created')
                    department.ministry = ministry
                    department.save()
                    # department, created = Department.objects.update_or_create(department_name = row['Department'],
                    #                                                           defaults='ministry':ministry
                    #                                                           )

        return JsonResponse({'okay':'okay'})