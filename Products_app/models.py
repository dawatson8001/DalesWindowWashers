# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from settings import staging


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": staging.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "GBP",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": staging.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % staging.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % staging.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.name
