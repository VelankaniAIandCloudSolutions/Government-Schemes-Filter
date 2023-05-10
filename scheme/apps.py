from django.apps import AppConfig


class SchemeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheme'

    def ready(self):
        from .app_init import create_castes, create_disability, create_education,create_genders,create_marital_status,create_occupations, create_states, create_age_groups, create_income_groups
        create_castes()
        create_disability()
        create_education()
        create_genders()
        create_marital_status()
        create_occupations()
        create_states()
        create_age_groups()
        create_income_groups()
        # for state in STATE_CHOICES:
        #     State.objects.get_or_create(name=state[0])
