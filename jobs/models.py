from django.db import models

class JobOffer(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name