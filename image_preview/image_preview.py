"""
Image preview plugin for pelican
"""
from bs4 import BeautifulSoup
from pelican import signals
import logging
log = logging.getLogger(__name__)

def find_preview(instance):
    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content)
        log.info(soup)
        img = soup.find('img')
        if img is None:
            return

        source = img['src']
        instance.preview_image = source

def register():
    signals.content_object_init.connect(find_preview)