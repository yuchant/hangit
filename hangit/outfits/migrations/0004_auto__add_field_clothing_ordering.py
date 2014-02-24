# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Clothing.ordering'
        db.add_column(u'outfits_clothing', 'ordering',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Clothing.ordering'
        db.delete_column(u'outfits_clothing', 'ordering')


    models = {
        u'outfits.clothing': {
            'Meta': {'object_name': 'Clothing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['outfits.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'outfits.outfit': {
            'Meta': {'object_name': 'Outfit'},
            'accessory': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'accessory'", 'null': 'True', 'to': u"orm['outfits.Clothing']"}),
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
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['outfits.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
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