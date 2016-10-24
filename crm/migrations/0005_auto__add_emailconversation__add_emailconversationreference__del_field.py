# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailConversation'
        db.create_table(u'crm_emailconversation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email_account', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'email_conversation_set', to=orm['crm.EmailAccount'])),
            ('case', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Case'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
        ))
        db.send_create_signal(u'crm', ['EmailConversation'])

        # Adding model 'EmailConversationReference'
        db.create_table(u'crm_emailconversationreference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email_conversation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.EmailConversation'], null=True, blank=True)),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=256, db_index=True)),
        ))
        db.send_create_signal(u'crm', ['EmailConversationReference'])

        # Deleting field 'Email.case'
        db.delete_column(u'crm_email', 'case_id')

        # Adding field 'Email.email_conversation'
        db.add_column(u'crm_email', 'email_conversation',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.EmailConversation'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Email.message_id'
        db.add_column(u'crm_email', 'message_id',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'EmailConversation'
        db.delete_table(u'crm_emailconversation')

        # Deleting model 'EmailConversationReference'
        db.delete_table(u'crm_emailconversationreference')

        # Adding field 'Email.case'
        db.add_column(u'crm_email', 'case',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Case'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Email.email_conversation'
        db.delete_column(u'crm_email', 'email_conversation_id')

        # Deleting field 'Email.message_id'
        db.delete_column(u'crm_email', 'message_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'crm.account': {
            'Meta': {'object_name': 'Account'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'crm.case': {
            'Meta': {'object_name': 'Case'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Account']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'crm.contact': {
            'Meta': {'object_name': 'Contact'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Account']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'www': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'crm.email': {
            'Meta': {'object_name': 'Email'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'email_set'", 'to': u"orm['crm.EmailAccount']"}),
            'email_conversation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.EmailConversation']", 'null': 'True', 'blank': 'True'}),
            'email_from': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'email_to': ('django.db.models.fields.EmailField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'crm.emailaccount': {
            'Meta': {'object_name': 'EmailAccount'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imap_host': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'imap_password': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'imap_port': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'imap_tls': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'imap_user': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'smtp_host': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'smtp_password': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'smtp_port': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'smtp_tls': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'smtp_user': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'crm.emailaccountfolder': {
            'Meta': {'object_name': 'EmailAccountFolder'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'folder_set'", 'to': u"orm['crm.EmailAccount']"}),
            'folder': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'crm.emailconversation': {
            'Meta': {'object_name': 'EmailConversation'},
            'case': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Case']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'email_conversation_set'", 'to': u"orm['crm.EmailAccount']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'crm.emailconversationreference': {
            'Meta': {'object_name': 'EmailConversationReference'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_conversation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.EmailConversation']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_index': 'True'})
        }
    }

    complete_apps = ['crm']