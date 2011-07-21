import settings
from django.template.loader import get_template
from django.template import Context
from xhtml2pdf import pisa
import cStringIO as StringIO
import cgi


def render_invoice(invoice):
    description = invoice
    amount = invoice.subscription.product.price
    tax = amount * 0.19
    total = amount + tax
    template = 'invoices/detail.html'
    context_dict = {
        'username': invoice.subscription.user.username,
        'first_name': invoice.subscription.user.first_name,
        'last_name': invoice.subscription.user.last_name,
        'email': invoice.subscription.user.email,
        'date': invoice.date,
        'description': description,
        'amount': "%0.2f" % amount,
        'tax': "%0.2f" % tax,
        'total': "%0.2f" % total,
        'MEDIA_ROOT': settings.MEDIA_ROOT,
    }
    template = get_template(template)
    context = Context(context_dict)
    return template.render(context)


def make_pdf(html):
    result = StringIO.StringIO()
    pdf = pisa.CreatePDF(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    return result.getvalue()

