# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CharacterClass'
        db.create_table('class', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('alignment', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('hit_die', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('class_skills', self.gf('django.db.models.fields.TextField')()),
            ('skill_points', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('skill_points_ability', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('spell_stat', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('proficiencies', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spell_type', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('epic_feat_base_level', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('epic_feat_interval', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('epic_feat_list', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('epic_full_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('req_race', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('req_weapon_proficiency', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('req_base_attack_bonus', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('req_skill', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('req_feat', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('req_spells', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('req_languages', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('req_psionics', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('req_epic_feat', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('req_special', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('spell_list_1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('spell_list_2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('spell_list_3', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('spell_list_4', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('spell_list_5', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('full_text', self.gf('django.db.models.fields.TextField')()),
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('srd20', ['CharacterClass'])


    def backwards(self, orm):
        
        # Deleting model 'CharacterClass'
        db.delete_table('class')


    models = {
        'srd20.characterclass': {
            'Meta': {'ordering': "('name',)", 'object_name': 'CharacterClass', 'db_table': "'class'"},
            'alignment': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'class_skills': ('django.db.models.fields.TextField', [], {}),
            'epic_feat_base_level': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'epic_feat_interval': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'epic_feat_list': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'epic_full_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'full_text': ('django.db.models.fields.TextField', [], {}),
            'hit_die': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'proficiencies': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'req_base_attack_bonus': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'req_epic_feat': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'req_feat': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'req_languages': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'req_psionics': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'req_race': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'req_skill': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'req_special': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'req_spells': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'req_weapon_proficiency': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'skill_points': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'skill_points_ability': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'spell_list_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'spell_list_2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'spell_list_3': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'spell_list_4': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'spell_list_5': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'spell_stat': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'spell_type': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'srd20.feat': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Feat', 'db_table': "'feat'"},
            'altname': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'benefit': ('django.db.models.fields.TextField', [], {}),
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multiple': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'normal': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prerequisite': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'special': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stack': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'srd20.spell': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Spell', 'db_table': "'spell'"},
            'altname': ('django.db.models.fields.SlugField', [], {'max_length': '64', 'db_index': 'True'}),
            'arcane_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'arcane_material_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'casting_time': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'cleric_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'components': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'descriptor': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'druid_focus': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'effect': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'focus': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'material_components': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'range': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'saving_throw': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'spell_resistance': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'spellcraft_dc': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'subschool': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'target': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'to_develop': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'verbal_components': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'xp_cost': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['srd20']
