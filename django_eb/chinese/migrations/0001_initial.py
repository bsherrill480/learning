# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChineseDialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('audio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChineseExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChineseGrammar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(unique=True)),
                ('grammar_rule', models.TextField()),
                ('examples', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChineseLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChineseVocabItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(unique=True)),
                ('pinyin', models.CharField(max_length=50)),
                ('word', models.CharField(max_length=50)),
                ('definition', models.TextField()),
                ('chinese_lesson', models.ForeignKey(to='chinese.ChineseLesson')),
            ],
        ),
        migrations.AddField(
            model_name='chinesegrammar',
            name='chinese_lesson',
            field=models.ForeignKey(to='chinese.ChineseLesson'),
        ),
        migrations.AddField(
            model_name='chineseexample',
            name='chinese_lesson',
            field=models.ForeignKey(to='chinese.ChineseLesson'),
        ),
    ]
