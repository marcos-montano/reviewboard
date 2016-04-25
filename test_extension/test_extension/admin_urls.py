from __future__ import unicode_literals

from django.conf.urls import patterns, url

from test_extension.extension import TestExtension


urlpatterns = patterns(
    'test_extension.views',

    url(r'^$', 'configure'),
)