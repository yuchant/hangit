from django.db import models


class Tag(models.Model):
	name = models.CharField(max_length=64)
	def __unicode__(self):
		return self.name


class Clothing(models.Model):
	'''
	An article of clothing
	'''
	name = models.CharField(max_length=64)
	image = models.ImageField(upload_to='images/clothing')
	TYPE_CHOICES = [(x, x) for x in (
		'hat',
		'jacket',
		'head',
		'neck',
		'torso',
		'waist',
		'feet',
	)]
	tags = models.ForeignKey(Tag)
	type = models.CharField(max_length=64, choices=TYPE_CHOICES)

	def __unicode__(self):
		return self.name


class Outfit(models.Model):
	scheduled_date = models.DateField(blank=True, null=True)
	name = models.CharField(max_length=256, blank=True)
	photo = models.ImageField(blank=True, null=True, upload_to='images/outfit')

	hat = models.ForeignKey(Clothing, blank=True, null=True, related_name='hats')
	jacket = models.ForeignKey(Clothing, blank=True, null=True, related_name='jackets')
	head = models.ForeignKey(Clothing, blank=True, null=True, related_name='head')
	neck = models.ForeignKey(Clothing, blank=True, null=True, related_name='neck')
	torso = models.ForeignKey(Clothing, blank=True, null=True, related_name='torso')
	waist = models.ForeignKey(Clothing, blank=True, null=True, related_name='waist')
	legs = models.ForeignKey(Clothing, blank=True, null=True, related_name='legs')
	feet = models.ForeignKey(Clothing, blank=True, null=True, related_name='feet')

	tags = models.ManyToManyField(Tag)

	def __unicode__(self):
		return self.name
