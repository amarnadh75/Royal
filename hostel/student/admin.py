from django.contrib import admin
from .models import product,Order

# Register your models here.
admin.site.site_header = "E-commerce"
admin.site.site_title = "Shopping"
admin.site.index_title = "Manage Shopping"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title','price','discount_price','category','description')
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    fields = ('title','price',)
    list_editable = ('price','category',)

admin.site.register(product,ProductAdmin)
admin.site.register(Order)


