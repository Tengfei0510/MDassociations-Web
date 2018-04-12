from django.db import models

class LncCeRBase(models.Model):
    lncrnas = models.CharField(max_length=100,verbose_name="LncRNA")
    mirnas = models.CharField(max_length=100,verbose_name="MiRNA")
    genes = models.CharField(max_length=100,verbose_name="Gene")
    gene_ids = models.CharField(max_length=200,verbose_name="Gene Name (All)",null=True,blank=True)
    pathway_name = models.TextField(verbose_name="Pathway Name",null=True,blank=True)
    diseases = models.CharField(max_length=100,verbose_name="Disease/Tissue")
    Description = models.TextField(verbose_name="Description",null=True,blank=True)
    PubMed_ID = models.CharField(max_length=100,verbose_name="PubMed_ID")
    Year = models.IntegerField(verbose_name="Year",default=2017)
    Journal = models.CharField(max_length=100,verbose_name="Journal")
    Title = models.TextField(verbose_name="Title",null=True,blank=True)

    def __str__(self):
        return self.lncrnas + '---' + self.mirnas

# Create your models here.
