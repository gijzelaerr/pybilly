from django.contrib import admin
from invoices.models import Invoice, Product, Subscription


class InvoiceAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class SubscriptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Subscription, SubscriptionAdmin)

