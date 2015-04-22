import time
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import get_valid_filename, slugify
from django.utils.encoding import python_2_unicode_compatible


EXTENSION_CHOICES = (
    ('.ini', _('INI file')),
    ('.yml', _('YAML file')),
    ('.xml', _('XML file')),
    ('.json', _('JSON file')),
)


@python_2_unicode_compatible
class Vassal(models.Model):
    """
    Model for uWSGI Vassals
    """
    title = models.CharField(
        _('Name'),
        max_length=250
    )
    name = models.CharField(
        _('Filename'),
        help_text=_('Name of uwsgi config file'),
        max_length=255,
        db_column='name',
        editable=False
    )
    extension = models.CharField(
        _('Extension'),
        max_length=4,
        default=EXTENSION_CHOICES[0],
        choices=EXTENSION_CHOICES
    )
    config = models.TextField(
        _('Config'),
        help_text=_('Config file blob'),
        db_column='config'
    )
    ts = models.FloatField(
        _('Unix Timestamp'),
        help_text=_('A number representing the modification time of this row in UNIX format'),
        db_column='ts',
        editable=False
    )
    uid = models.PositiveSmallIntegerField(
        _('The UID of the vassal instance'),
        help_text=_('Required in Tyrant mode (secure multi-user hosting) mode only.'),
        db_column='uid',
        blank=True,
        null=True
    )
    gid = models.PositiveSmallIntegerField(
        _('The GID of the vassal instance'),
        help_text=_('Required in Tyrant mode (secure multi-user hosting) mode only.'),
        db_column='gid',
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        _('Created at'),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        _('Updated'),
        auto_now=True,
        blank=True,
        null=True
    )
    enabled = models.BooleanField(
        _('Enabled'),
        default=True
    )


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.name = get_valid_filename(slugify(self.title) + self.extension)
        self.ts = time.time()
        super(Vassal, self).save(*args, **kwargs)


    class Meta:
        verbose_name = _("Emperor's Vassal")
        verbose_name_plural = _("Emperor's Vassals")
        db_table = 'vassals'
