# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Clothing.tags'
        db.delete_column(u'outfits_clothing', 'tags_id')

        # Adding M2M table for field tags on 'Clothing'
        m2m_table_name = db.shorten_name(u'outfits_clothing_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('clothing', models.ForeignKey(orm[u'outfits.clothing'], null=False)),
            ('tag', models.ForeignKey(orm[u'outfits.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['clothing_id', 'tag_id'])


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Clothing.tags'
        raise RuntimeError("Cannot reverse this migration. 'Clothing.tags' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Clothing.tags'
        db.add_column(u'outfits_clothing', 'tags',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['outfits.Tag']),
                      keep_default=False)

        # Removing M2M table for field tags on 'Clothing'
        db.delete_table(db.shorten_name(u'outfits_clothing_tags'))


    models = {
        u'outfits.clothing': {
            'Meta': {'object_name': 'Clothing'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['outfits.Tag']", 'symmetrical': 'False'}),
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