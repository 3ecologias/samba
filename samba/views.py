# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactUs, SignUp
from django.contrib.auth.models import User
from samba.plan.plugins import get_all_plugins
from samba.plan.models import Plano

from urllib.request import urlopen
from urllib.parse import urlencode
import urllib
import json
from django.conf import settings

class Index(FormView):
	template_name = "index.html"
	form_class = ContactUs
	success_url = '/'

	def get_context_data(self, **kwargs):

		ctx = super(Index, self).get_context_data(**kwargs)
		ctx.update({
			'plans': Plano.objects.all(),
		})

		return ctx

	def form_valid(self, form):
		form.send_email()

		return super(Index, self).form_valid(form)

class ToolsView(TemplateView):
	template_name = 'tools.html'

	def get_context_data(self, **kwargs):
		ctx = super(TemplateView, self).get_context_data(**kwargs)
		plugins = get_all_plugins()

		ctx.update({
			'plugins': plugins,
		})

		return ctx

# class SignUp(FormView):
# 	template_name = "signup.html"
# 	form_class = SignUp
# 	success_url = '/signup'
#
# 	def get_context_data(self, **kwargs):
#
# 		context = super(SignUp, self).get_context_data(**kwargs)
#
# 		return context
#
# 	def form_valid(self, form):
# 		form.send_email()
#
# 		return super(SignUp, self).form_valid(form)

	# def form_valid(self, form):
	# 	''' Begin reCAPTCHA validation '''
	# 	recaptcha_response = self.request.POST.get('g-recaptcha-response')
	# 	url = 'https://www.google.com/recaptcha/api/siteverify'
	# 	values = {
	# 		'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
	# 		'response': recaptcha_response
    #     }
	# 	data = urlencode(values)
	# 	req = urllib.request.Request(url, data)
	# 	response = urlopen(req)
	# 	result = json.load(response)
	# 	''' End reCAPTCHA validation '''
	# 	if result['success']:
	# 		form.send_email()
	# 		messages.success(self.request, 'Seu contato foi enviado com sucesso!')
	# 	else:
	# 		messages.error(self.request, 'reCAPTCHA inválida. Por favor, tente novamente.')
	# 		return HttpResponseRedirect(super(Index, self).get_success_url())
	#
	# 	return super(Index, self).form_valid(form)
	#
