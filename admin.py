from django.contrib import admin
from job.models import JobPost, JobCategory, JobType, Company, CompanyCategory, CompanyLocation

class JobPostAdmin(admin.ModelAdmin):
     list_display = ('postdate', 'title', 'company', 'poster', 'category','jobtype','description','requirement','application')
     list_filter = ['category']
class JobCategoryAdmin(admin.ModelAdmin):
     list_display = ['name']
class JobTypeAdmin(admin.ModelAdmin):
     list_display = ['name']
class CompanyAdmin(admin.ModelAdmin):
     list_display = ('name', 'description', 'phone', 'fax', 'email','website','person','poster')
     list_filter = ['poster']
class CompanyCategoryAdmin(admin.ModelAdmin):
     list_display = ['name']
class CompanyLocationAdmin(admin.ModelAdmin):
     list_display = ['name']

admin.site.register(JobPost, JobPostAdmin)
admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(JobType, JobTypeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyCategory, CompanyCategoryAdmin)
admin.site.register(CompanyLocation, CompanyLocationAdmin)
