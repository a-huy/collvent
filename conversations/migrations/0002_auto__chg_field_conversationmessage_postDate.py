# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ConversationMessage.postDate'
        db.alter_column(u'conversations_conversationmessage', 'postDate', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'ConversationMessage.postDate'
        db.alter_column(u'conversations_conversationmessage', 'postDate', self.gf('django.db.models.fields.DateTimeField')(default=''))

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
        u'conversations.conversation': {
            'Meta': {'object_name': 'Conversation'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'conversations.conversationcontent': {
            'Meta': {'object_name': 'ConversationContent'},
            'conversation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['conversations.Conversation']"}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'conversations.conversationmessage': {
            'Meta': {'object_name': 'ConversationMessage'},
            'conversation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['conversations.Conversation']"}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"}),
            'postDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'deleted_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'deleted_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'db_index': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '512'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Place']"}),
            'modified_by': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'})
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
            'tester': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['conversations']