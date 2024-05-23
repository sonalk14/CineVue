from django.contrib import admin
from.models import Movie,Wishlist,Subscriptions,Suborder

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display=["m_id","name"]
admin.site.register(Movie,MovieAdmin)
admin.site.register(Wishlist)

class SubAdmin(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Subscriptions,SubAdmin)

admin.site.register(Suborder)

