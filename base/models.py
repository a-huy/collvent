from django.db import models, DatabaseError
import django.utils.timezone
from base.managers import ActiveManager, VanishedManager
from accounts.constants import USER_HASH_MAX_LENGTH

import datetime
import pretty

class Base(models.Model):
    created_date = models.DateTimeField(editable=False, default=django.utils.timezone.now)
    modified_date = models.DateTimeField(default=django.utils.timezone.now)
    deleted_date = models.DateTimeField(null=True, default=None, db_index=True)
    created_by = models.CharField(max_length=USER_HASH_MAX_LENGTH, editable=False)
    modified_by = models.CharField(max_length=USER_HASH_MAX_LENGTH, editable=False, null=True)
    deleted_by = models.CharField(max_length=USER_HASH_MAX_LENGTH, editable=False, null=True)

    objects = models.Manager()
    active = ActiveManager()
    vanished = VanishedManager()

    class Meta:
        abstract = True

    @property
    def last_modified(self):
        if self.deleted_date:
            return max(self.modified_date, self.deleted_date)
        return self.modified_date

    def save(self, *args, **kwargs):
        saved_by = kwargs.pop('saved_by', None)
        if saved_by:
            self.modified_by = saved_by
            self.modified_date = django.utils.timezone.now()
            if not self.pk or 'force_insert' in kwargs and kwargs['force_insert']:
                self.created_by = saved_by
        self.__save(*args, **kwargs)

    def vanish(self, *args, **kwargs):
        deleted_by = kwargs.pop('deleted_by', None)
        deleted_date = kwargs.pop('deleted_date', None) or django.utils.timezone.now()
        if deleted_by:
            self.deleted_by = deleted_by
        else:
            self.deleted_by = ':system:'
        self.deleted_date = deleted_date
        self.__save(*args, **kwargs)

    def unvanish(self, *args, **kwargs):
        self.deleted_by = None
        self.deleted_date = None
        self.__save(*args, **kwargs)

    def __save(self, *args, **kwargs):
        try:
            super(Base, self).save(*args, **kwargs)
        except DatabaseError, err:
            raise

    def get_created_date_friendly(self):
        print "PRETTY: ", pretty.date(self.created_date)
        return "TEST"