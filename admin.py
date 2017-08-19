from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Cat,CatColony,CatCaretaker,CatLogEntry,CatVaccines,CatParasites


# Register your models here.
admin.site.register(Cat,SimpleHistoryAdmin)
admin.site.register(CatColony,SimpleHistoryAdmin)
admin.site.register(CatCaretaker,SimpleHistoryAdmin)
admin.site.register(CatLogEntry,SimpleHistoryAdmin)
admin.site.register(CatVaccines)
admin.site.register(CatParasites)



