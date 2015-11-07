from django.contrib import admin

# Register your models here.
from atus.models import Respondant, Activity, Household

admin.site.register(Respondant)
admin.site.register(Activity)
admin.site.register(Household)
