# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from indisposable_email_field.models import DisposableDomainName
from indisposable_email_field.data import domain_names


class Migration(SchemaMigration):
    def forwards(self, orm):
        ddns = [DisposableDomainName(value=name) for name in domain_names]
        DisposableDomainName.objects.bulk_create(ddns)

    def backwards(self, orm):
        DisposableDomainName.objects.filter(value__in=domain_names).delete()

    models = {
        u'indisposable_email_field.disposabledomainname': {
            'Meta': {'object_name': 'DisposableDomainName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'})
        }
    }

    complete_apps = ['indisposable_email_field']
