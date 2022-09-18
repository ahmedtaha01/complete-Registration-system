from django.db import models
from categories.models import Category

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=100, help_text='Project title should not exceed 100 character.')
    project_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    project_details = models.TextField(null=True)
    project_total_target = models.IntegerField(null=True)
    project_start_date = models.DateField(null=True, blank=True)
    project_end_date = models.DateField(null=True, blank=True) 
    # project_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_title


class Images(models.Model):
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/imgs',null=True,blank=True)
