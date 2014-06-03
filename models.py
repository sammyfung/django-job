from django.db import models
from django.contrib.auth.models import User

class JobPost(models.Model):
  postdate = models.DateTimeField()
  title = models.CharField(max_length=128)
  company = models.ForeignKey('job.Company',null=True, blank=True)
  poster = models.ForeignKey(User)
  category = models.ForeignKey('job.JobCategory',null=True, blank=True)
  jobtype = models.ForeignKey('job.JobType',null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  requirement = models.TextField()
  application = models.TextField(null=True, blank=True)

  def __unicode__(self):
    return self.title

class JobCategory(models.Model):
  name = models.CharField(max_length=64)

  def __unicode__(self):
    return self.name

class JobType(models.Model):
  name = models.CharField(max_length=64)

  def __unicode__(self):
    return self.name

class Company(models.Model):
  name = models.CharField(max_length=128)
  description = models.TextField(null=True, blank=True)
  phone = models.CharField(max_length=32, null=True, blank=True)
  fax = models.CharField(max_length=32, null=True, blank=True)
  email = models.CharField(max_length=128, null=True, blank=True)
  website = models.CharField(max_length=128, null=True, blank=True)
  person = models.CharField(max_length=64, null=True, blank=True)
  poster = models.ForeignKey(User)
  category = models.ForeignKey('job.CompanyCategory', null=True, blank=True)
  location = models.ForeignKey('job.CompanyLocation', null=True, blank=True)

  def __unicode__(self):
    return self.name

class CompanyCategory(models.Model):
  name = models.CharField(max_length=128)

  def __unicode__(self):
    return self.name

class CompanyLocation(models.Model):
  name = models.CharField(max_length=128)

  def __unicode__(self):
    return self.name

