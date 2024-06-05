from django.contrib import admin

from charity_app.models import Category, Institution, Donation


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    pass