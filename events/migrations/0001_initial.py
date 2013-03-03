# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'events_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('modified_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('deleted_date', self.gf('django.db.models.fields.DateField')(default=None, null=True, db_index=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('deleted_by', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('street_addr', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('zip_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=31, null=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=31, null=True)),
        ))
        db.send_create_signal(u'events', ['Place'])

        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('modified_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('deleted_date', self.gf('django.db.models.fields.DateField')(default=None, null=True, db_index=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('deleted_by', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=512)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Place'])),
        ))
        db.send_create_signal(u'events', ['Event'])

        # Adding model 'Invitation'
        db.create_table(u'events_invitation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('modified_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('deleted_date', self.gf('django.db.models.fields.DateField')(default=None, null=True, db_index=True)),
            ('created_by', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('modified_by', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('deleted_by', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'])),
        ))
        db.send_create_signal(u'events', ['Invitation'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'events_place')

        # Deleting model 'Event'
        db.delete_table(u'events_event')

        # Deleting model 'Invitation'
        db.delete_table(u'events_invitation')


    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'avatar': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '31', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Place']"}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'events.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"})
        },
        u'events.place': {
            'Meta': {'object_name': 'Place'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '31', 'null': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'street_addr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['events']