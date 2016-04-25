# TestExtension Extension for Review Board.

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import SignalHook
from reviewboard.reviews.signals import review_request_published

import logging


class TestExtension(Extension):
    metadata = {
        'Name': 'TestExtension',
        'Summary': 'First Test Extension.',
    }

    def initialize(self):
        SignalHook(self, review_request_published, self.on_published)

    def on_published(self, review_request=None, **kwargs):
        logging.info('!!!!!!!!!!!!!!!!!!!!!! 1 ')
        logging.info('Review request %s was published!', review_request.display_id)
        logging.info('review_request.summary: %s', review_request.summary)
        logging.info('review_request.target_people: %s', review_request.target_people)
        logging.info('review_request.target_people: %s', review_request.target_people.all())
        logging.info('review_request.target_groups: %s', review_request.target_groups.all())
        logging.info('kwargs: %s', kwargs)
        logging.info('review_request: %s', review_request)
        review_request.summary = 'New Summary'
        review_request.save()
        logging.info('review_request.summary: %s', review_request.summary)
        logging.info('!!!!!!!!!!!!!!!!!!!!!! 2 ')

