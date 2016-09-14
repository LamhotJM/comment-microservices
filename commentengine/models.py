from __future__ import unicode_literals
from django.db import models


class MasterComment(models.Model):
    commentid = models.BigIntegerField(primary_key=True)
    userid = models.CharField(blank=True, null=True, max_length=100)
    loanid = models.CharField(blank=True, null=True, max_length=100)
    comment = models.TextField()
    createdby = models.CharField(blank=True, null=True, max_length=25)
    createddate = models.DateTimeField()
    createdfrom = models.CharField(blank=True, null=True, max_length=60)
    modifiedby = models.CharField(blank=True, null=True, max_length=25)
    modifieddate = models.DateTimeField()
    modifiedfrom = models.CharField(blank=True, null=True, max_length=60)

    class Meta:
        managed = False
        db_table = 'comments'

    def __unicode__(self):
        return u'%d: %s' % (self.id, self.type)
