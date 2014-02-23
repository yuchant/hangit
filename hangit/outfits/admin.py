from django.contrib import admin
from outfits import models


class ClothingAdmin(admin.ModelAdmin):
	list_display = ('name', 'type', )


class TagAdmin(admin.ModelAdmin):
	pass


class OutfitAdmin(admin.ModelAdmin):
	pass


admin.site.register(models.Clothing, ClothingAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Outfit, OutfitAdmin)
