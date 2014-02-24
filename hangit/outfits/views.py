from django.shortcuts import render
from django.views import generic

from outfits import models


class IndexView(generic.TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		ctx = super(IndexView, self).get_context_data(**kwargs)
		ctx['outfits'] = models.Outfit.objects.all().order_by('scheduled_date')
		return ctx



class ClothingView(generic.TemplateView):
	template_name = 'clothing.html'

	def get_context_data(self, **kwargs):
		ctx = super(ClothingView, self).get_context_data(**kwargs)
		ctx['clothings'] = models.Clothing.objects.all().order_by('-type')
		return ctx


class OutfitView(generic.UpdateView):
	template_name = 'outfit.html'
	model = models.Outfit
	success_url = '/'

	def get_context_data(self, **kwargs):
		ctx = super(OutfitView, self).get_context_data(**kwargs)
		# ctx['clothings'] = models.Clothing.objects.all()
		return ctx
	