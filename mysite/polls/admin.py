from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['question']}),
		('Fecha', 	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date') #Si aniadimos was_published_today salta un error de que la variable global datetime no esta definida.

admin.site.register(Poll, PollAdmin)
