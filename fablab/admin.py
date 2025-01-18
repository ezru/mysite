from django.contrib import admin
from .models import Users, Items, ItemLoan, Booking

admin.site.register(Users)
admin.site.register(Items)
admin.site.register(ItemLoan)
admin.site.register(Booking)
