"""
Text summary plugin for pelican
"""
from bs4 import BeautifulSoup
from pelican import signals
import logging
log = logging.getLogger(__name__)

def redo_summary(instance):
    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content)
        [s.extract() for s in soup('img')]
        instance.text_summary = str(soup)

def register():
    signals.content_object_init.connect(redo_summary)