"""
Text summary plugin for pelican
"""
from bs4 import BeautifulSoup
from pelican import signals
from pelican.utils import truncate_html_words
import logging
log = logging.getLogger(__name__)

SUMMARY_MAX_LENGTH = 50

def redo_summary(instance):
    summary = ""
    if 'summary' in instance.metadata:
        summary = instance.metadata.get('summary')
    elif hasattr(instance, "_summary") and instance._summary is not None:
        summary = instance._summary
    elif hasattr(instance, "_content") and instance._content is not None:
        summary_max_length = instance._context.get("SUMMARY_MAX_LENGTH", SUMMARY_MAX_LENGTH)
        summary = truncate_html_words(instance._content, summary_max_length)

    soup = BeautifulSoup(summary, from_encoding='utf-8')
    [s.extract() for s in soup('img')]
    instance.text_summary = soup

def register():
    signals.content_object_init.connect(redo_summary)