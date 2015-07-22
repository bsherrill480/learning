from django.db import models

class ChineseLesson(models.Model):
    lesson_number = models.IntegerField(unique=True) #not going to make lesson_number a primary key, because what if I want to
                                          #move lessons around

class ChineseVocabItem(models.Model):
    #id should be used for implicit order
    chinese_lesson = models.ForeignKey(ChineseLesson)
    order = models.IntegerField(unique=True)
    pinyin = models.CharField(max_length=50)
    word = models.CharField(max_length=50)
    definition = models.TextField()

class ChineseExample(models.Model):
    chinese_lesson = models.ForeignKey(ChineseLesson)
    order = models.IntegerField(unique=True)

class ChineseGrammar(models.Model):
    chinese_lesson = models.ForeignKey(ChineseLesson)
    order = models.IntegerField(unique=True)
    grammar_rule = models.TextField()
    examples = models.TextField()

class ChineseDialog(models.Model):
    text = models.TextField()
    audio = models.CharField(max_length=100)
