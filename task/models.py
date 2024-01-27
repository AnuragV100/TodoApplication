from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    due_date=models.DateTimeField()
    complete_opt=(
        ("Not Completed","Not Completed"),
        ("Completed","Completed")
    )
    is_completed=models.CharField(max_length=200,choices=complete_opt,default="Not Completed")
    user=models.CharField(max_length=200)

    def __str__(self):
        return self.title
