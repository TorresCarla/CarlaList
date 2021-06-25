from django.contrib import admin
from .models import Loaner, SignUp, AmountLoan, Branches, Repayment

admin.site.register(Loaner)
admin.site.register(SignUp)
admin.site.register(AmountLoan)
admin.site.register(Branches)
admin.site.register(Repayment)

# Register your models here.
