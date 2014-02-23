# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'outfits_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'outfits', ['Tag'])

        # Adding model 'Clothing'
        db.create_table(u'outfits_clothing', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('tags', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['outfits.Tag'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'outfits', ['Clothing'])

        # Adding model 'Outfit'
        db.create_table(u'outfits_outfit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scheduled_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('hat', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='hats', null=True, to=orm['outfits.Clothing'])),
            ('jacket', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='jackets', null=True, to=orm['outfits.Clothing'])),
            ('head', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='head', null=True, to=orm['outfits.Clothing'])),
            ('neck', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='neck', null=True, to=orm['outfits.Clothing'])),
            ('torso', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='torso', null=True, to=orm['outfits.Clothing'])),
            ('waist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='waist', null=True, to=orm['outfits.Clothing'])),
            ('legs', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='legs', null=True, to=orm['outfits.Clothing'])),
            ('feet', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='feet', null=True, to=orm['outfits.Clothing'])),
        ))
        db.send_create_signal(u'outfits', ['Outfit'])

        # Adding M2M table for field tags on 'Outfit'
        m2m_table_name = db.shorten_name(u'outfits_outfit_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('outfit', models.ForeignKey(orm[u'outfits.outfit'], null=False)),
            ('tag', models.ForeignKey(orm[u'outfits.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['outfit_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'outfits_tag')

        # Deleting model 'Clothing'
        db.delete_table(u'outfits_clothing')

        # Deleting model 'Outfit'
        db.delete_table(u'outfits_outfit')

        # Removing M2M table for field tags on 'Outfit'
        db.delete_table(db.shorten_name(u'outfits_outfit_tags'))


    models = {
        u'outfits.clothing': {
            'Meta': {'object_name': 'Clothing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tags': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['outfits.Tag']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'outfits.outfit': {
            'Meta': {'object_name': 'Outfit'},
            'feet': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'feet'", 'null': 'True', 'to': u"orm['outfits.Clothing']"}),
            'hat': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hats'", 'null': 'True', 'to': u"orm['outfits.Clothing']"}),
            'head': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'head'", 'null': 'True', 'to': u"orm['outfits.Clothing']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jacket': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'jackets'", 'null': 'True', 'to': u"orm['outfits.Clothing']"}),
            'legs': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'legs'", 'null': 'True', 'to': u"orm['outfits.Clothing']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'neck': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'neck'", 'null': 'True', 'to': u"orm['outfits.Clothing']"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'scheduled_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['outfits.Tag']", 'symmetrical': 'False'}),
            'torso': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'torso'", 'null': 'True', 'to': u"orm['outfits.Clothing']"}),
            'waist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'waist'", 'null': 'True', 'to': u"orm['outfits.Clothing']"})
        },
        u'outfits.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['outfits']