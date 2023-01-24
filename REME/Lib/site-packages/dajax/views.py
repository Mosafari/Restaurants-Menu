# coding: utf-8
# Copyright (c) Alexandre Syenchuk (alexpirine), 2016

from __future__ import unicode_literals

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET

# Create your views here.

@require_GET
@cache_control(max_age=getattr(settings, 'DAJAX_CACHE_AGE', 3600))
def get_url(request, url_name):
    url_prefix = getattr(settings, 'DAJAX_URL_NAME_PREFIX', '')

    try:
        url = reverse(url_prefix+url_name, kwargs=request.GET.dict())
    except NoReverseMatch:
        return JsonResponse({
            'status': 'error',
            'error': _("Unable to resolve URL with specified arguments."),
        }, status=404)

    return JsonResponse({'status': 'ok', 'url': url})
