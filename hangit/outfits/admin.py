from django.contrib import admin
from outfits import models


class ClothingAdmin(admin.ModelAdmin):
    readonly_fields = ('_image',)
    list_display = ('name', 'type', '_image')

    def _image(self, obj):
        return '<img src="%s" style="max-height: 100px;" />' % obj.image.url
    _image.allow_tags = True

class TagAdmin(admin.ModelAdmin):
    pass



def render_image_field(obj, fieldname):
    field = getattr(obj, fieldname)
    if field:
        return '<img src="%s" style="max-height: 100px;" />' % field.image.url
    else:
        return ''


class OutfitAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'scheduled_date',
        '_hat',
        # '_head',
        # '_neck',
        '_jacket',
        '_torso',
        # '_waist',
        '_legs',
        '_feet',
        '_accessory',
    )
    list_display_links = list_display
    readonly_fields = (
        '_hat', '_jacket', '_head', '_neck', '_torso', '_waist', '_legs', '_feet', '_accessory'
    )

    ordering = ('scheduled_date', )
    def _hat(self, obj):
        return render_image_field(obj, 'hat')
    _hat.allow_tags = True

    def _jacket(self, obj):
        return render_image_field(obj, 'jacket')
    _jacket.allow_tags = True

    def _head(self, obj):
        return render_image_field(obj, 'head')
    _head.allow_tags = True

    def _neck(self, obj):
        return render_image_field(obj, 'neck')
    _neck.allow_tags = True

    def _torso(self, obj):
        return render_image_field(obj, 'torso')
    _torso.allow_tags = True

    def _waist(self, obj):
        return render_image_field(obj, 'waist')
    _waist.allow_tags = True

    def _legs(self, obj):
        return render_image_field(obj, 'legs')
    _legs.allow_tags = True

    def _feet(self, obj):
        return render_image_field(obj, 'feet')
    _feet.allow_tags = True

    def _accessory(self, obj):
        return render_image_field(obj, 'accessory')
    _accessory.allow_tags = True



admin.site.register(models.Clothing, ClothingAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Outfit, OutfitAdmin)
