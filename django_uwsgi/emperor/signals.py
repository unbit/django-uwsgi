from django.utils import timezone
from django.db.models.signals import post_save

#from .subscription import notify_vassal_subscribers
from .models import Vassal


def vassal_saved(instance, **kwargs):
    pass