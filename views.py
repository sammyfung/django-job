from django.shortcuts import render
from django.http import HttpResponse
from job.models import JobPost, JobCategory, JobType, Company, CompanyCategory, CompanyLocation

def index(request):
  latest_job = JobPost.objects.order('-postdate')[:10]
  output = ', '
  return HttpResponse(output)
