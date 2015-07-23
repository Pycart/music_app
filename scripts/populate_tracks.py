#!/usr/bin/env python
import requests

sys.path.append("..")  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import Genres  