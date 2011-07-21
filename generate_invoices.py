#!/usr/bin/env python

import sys, os
import datetime
from django.core.mail import EmailMessage
from invoices.tools import render_invoice, make_pdf

#here = os.path.dirname(__file__)
here = "."
sys.path.append(here)
sys.path.append(os.path.join(here, ".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.contrib.auth.models import User
from invoices.models import Subscription, Invoice, beginning_of_month

def mail_invoice(invoice):
    name = "%s %s" % (invoice.subscription.user.first_name, invoice.subscription.user.last_name)
    rcpt = invoice.subscription.user.email
    mail = EmailMessage(subject=str(invoice), body="", from_email='info@pythonic.nl', to=[rcpt])
    pdf = make_pdf(render_invoice(invoice))
    mail.attach('invoice.pdf',pdf,'application/pdf')
    mail.send()


for user in User.objects.filter(is_active=True):
    for subscription in user.subscriptions.filter(active=True):
        start = subscription.start
        end = subscription.end
        now = datetime.datetime.today().date()

        if end and end < now:
            print "warning: End date for user %s is passed but account still active" % user

        current = beginning_of_month(start)

        while current <= now:
            invoice, created = Invoice.objects.get_or_create(subscription=subscription,
                        date=current)
            if created:
                print "created %s" % invoice
                if invoice.subscription.user.email:
                    print "mailing %s" % invoice.subscription.user.email
                    mail_invoice(invoice)
                else:
                    print "warning: user doesn't have an email adress"

            current = beginning_of_month(current + datetime.timedelta(days=33))

