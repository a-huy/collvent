from django.db import models

# Create your models here.
class Base(models.Model):
        id = models.IntegerField(primary_key=True, auto_increment=True)
        created_date = models.DateField(editable=False, default=now())
        modified_date = models.DateField(default=now())
        deleted_date = models.DateField(null=True, default=None, db_index=True)
        created_by = models.CharField(null=True)
        modified_by = models.CharField(null=True)
        deleted_by = models.CharField(null=True)

        class Meta:
                abstract = True

