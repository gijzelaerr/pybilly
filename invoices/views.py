
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from invoices.models import Invoice


@login_required
def list(request):
    username = request.user.username
    invoices = Invoice.objects.all()
    return render_to_response('invoices/list.html', {'invoices': invoices},
            context_instance=RequestContext(request))


@login_required
def detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    username = request.user.username
    first_name = invoice.subscription.user.first_name
    last_name = invoice.subscription.user.last_name
    email = invoice.subscription.user.email
    date = invoice.date
    description = invoice
    amount = invoice.subscription.product.price
    tax = amount * 0.19
    total = amount + tax
    
    return render_to_response('invoices/detail.html',
                {   
                    'username': username,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'date': date,
                    'description': description,
                    'amount': "%0.2f" % amount,
                    'tax': "%0.2f" % tax,
                    'total': "%0.2f" % total,
                },
                context_instance=RequestContext(request)
            )

