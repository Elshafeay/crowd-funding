from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserModel


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = UserModel
	name = 'first_name' + ' ' + 'last_name'
	list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active',)
	list_filter = ('email', 'is_staff', 'is_active',)
	fieldsets = (
		(
			None,
			{
				'fields': (
					'first_name',
					'last_name',
					'email',
					'password',
					'country',
					'avatar',
					'phone',

				)
			}
		),
		('Permissions', {'fields': ('is_staff', 'is_active')}),
	)
	add_fieldsets = (
		(
			None,
			{
				'classes': ('wide',),
				'fields': (
					'first_name',
					'last_name',
					'email',
					'password1',
					'password2',
					'is_staff',
					'is_active',
					'country',
					'avatar',
					'phone',
				)
			}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)


admin.site.register(UserModel, CustomUserAdmin)
