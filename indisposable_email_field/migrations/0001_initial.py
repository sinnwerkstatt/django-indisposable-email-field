# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'DisposableDomainName'
        db.create_table(u'indisposable_email_field_disposabledomainname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=500)),
        ))
        db.send_create_signal(u'indisposable_email_field', ['DisposableDomainName'])

    def backwards(self, orm):
        # Deleting model 'DisposableDomainName'
        db.delete_table(u'indisposable_email_field_disposabledomainname')

    models = {
        u'indisposable_email_field.disposabledomainname': {
            'Meta': {'object_name': 'DisposableDomainName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'})
        }
    }

    complete_apps = ['indisposable_email_field']
