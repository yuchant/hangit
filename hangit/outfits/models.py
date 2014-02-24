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
		'legs',
		'feet',
		'accessory',
	)]
	ordering = models.IntegerField(default=0)
	tags = models.ManyToManyField(Tag, blank=True)
	type = models.CharField(max_length=64, choices=TYPE_CHOICES)

	class Meta:
		ordering = ['ordering']

	def __unicode__(self):
		return self.name


class Outfit(models.Model):
	scheduled_date = models.DateField(blank=True, null=True)
	name = models.CharField(max_length=256, blank=True)
	photo = models.ImageField(blank=True, null=True, upload_to='images/outfit')

	hat = models.ForeignKey(Clothing, blank=True, null=True, related_name='hats', limit_choices_to={'type': 'hat'})
	head = models.ForeignKey(Clothing, blank=True, null=True, related_name='head', limit_choices_to={'type': 'head'})
	neck = models.ForeignKey(Clothing, blank=True, null=True, related_name='neck', limit_choices_to={'type': 'neck'})
	jacket = models.ForeignKey(Clothing, blank=True, null=True, related_name='jackets', limit_choices_to={'type': 'jacket'})
	torso = models.ForeignKey(Clothing, blank=True, null=True, related_name='torso', limit_choices_to={'type': 'torso'})
	waist = models.ForeignKey(Clothing, blank=True, null=True, related_name='waist', limit_choices_to={'type': 'wait'})
	legs = models.ForeignKey(Clothing, blank=True, null=True, related_name='legs', limit_choices_to={'type': 'legs'})
	feet = models.ForeignKey(Clothing, blank=True, null=True, related_name='feet', limit_choices_to={'type': 'feet'})
	accessory = models.ForeignKey(Clothing, blank=True, null=True, related_name='accessory', limit_choices_to={'type': 'accessory'})

	tags = models.ManyToManyField(Tag, blank=True)

	def __unicode__(self):
		return self.name
