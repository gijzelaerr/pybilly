
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import http

from invoices.models import Invoice, Subscription
from invoices.tools import render_invoice, make_pdf
import settings



@login_required
def list(request):
    subscriptions = request.user.subscriptions.filter(active=True) 
    invoices = Invoice.objects.filter(subscription=subscriptions)
    return render_to_response('invoices/list.html', {'invoices': invoices},
            context_instance=RequestContext(request))


@login_required
def detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    html = render_invoice(invoice)
    pdf = make_pdf(html)
   
    return http.HttpResponse(pdf, mimetype='application/pdf')


