# TestExtension Extension for Review Board.

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include
from reviewboard.extensions.base import Extension
from reviewboard.extensions.hooks import SignalHook
from reviewboard.reviews.signals import review_request_published

from reviewboard.extensions.hooks import ReviewRequestFieldsHook
from reviewboard.reviews.fields import BaseEditableField, BaseTextAreaField, BaseReviewRequestField

import logging

class MilestoneField(BaseEditableField):
    field_id = 'cirrus_milestone'
    label = 'Milestone'


class NotesField(BaseTextAreaField):
    field_id = 'cirrus_notes'
    label = 'Notes'

class AssignedReviewerField(BaseReviewRequestField):
    field_id = 'cirrus_assigned_reviewer'
    label = 'Assigned Reviewer'
    #default_css_classes = []
    #is_editable = False

class TestExtension(Extension):
    metadata = {
        'Name': 'TestExtension',
        'Summary': 'First Test Extension.',
    }

    def initialize(self):
        # the signal hook
        SignalHook(self, review_request_published, self.on_published)
        # new fields hook
        ReviewRequestFieldsHook(self, 'info', [MilestoneField])
        ReviewRequestFieldsHook(self, 'main', [NotesField])
        ReviewRequestFieldsHook(self, 'reviewers', [AssignedReviewerField])

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
        review_request.extra_data['cirrus_assigned_reviewer'] = 'Nadim'
        review_request.save()
        logging.info('review_request.summary: %s', review_request.summary)
        logging.info('!!!!!!!!!!!!!!!!!!!!!! 2 ')

# from reviewboard.extensions.base import Extension
# from reviewboard.extensions.hooks import ReviewRequestFieldsHook
# from reviewboard.reviews.fields import BaseEditableField, BaseTextAreaField
#
#
# class MilestoneField(BaseEditableField):
#     field_id = 'myvendor_milestone'
#     label = 'Milestone'
#
#
# class NotesField(BaseTextAreaField):
#     field_id = 'myvendor_notes'
#     label = 'Notes'
#
#
# class SampleExtension(Extension):
#     def initialize(self):
#         ReviewRequestFieldsHook(self, 'info', [MilestoneField])
#         ReviewRequestFieldsHook(self, 'main', [NotesField])