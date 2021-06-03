from django.contrib import admin
from .models import Loaner, Item, AmountLoan, Branches, Repayment

admin.site.register(Loaner)
admin.site.register(Item)
admin.site.register(AmountLoan)
admin.site.register(Branches)
admin.site.register(Repayment)

# Register your models here.