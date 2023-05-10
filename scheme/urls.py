from django.urls import path

from . import views

urlpatterns = [
    path('my-api-form', views.filter_wix_data, name='filterWixData'),
    path('get-beneficiaries', views.get_beneficiaries, name='getBeneficiaries'),
    # path('import-data', views.import_data, name='importData'),
    path('import-beneficiaries', views.import_beneficiaries, name='importBeneficiaries'),
    path('import-schemes', views.import_schemes, name='importSchemes'),
    path('format-budget', views.format_budget, name='formatBudget'),
    path('import-departments', views.import_departments, name='importDepartments'),
]