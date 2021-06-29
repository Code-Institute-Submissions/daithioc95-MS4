from django.db import models


class Product(models.Model):
    Period = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=99)
    name = models.CharField(max_length=254, null=True, blank=True)
    Artist_Display_Name = models.CharField(max_length=254, null=True, blank=True)
    Artist_Display_Bio = models.CharField(max_length=254, null=True, blank=True)
    Artist_Alpha_Sort = models.CharField(max_length=254, null=True, blank=True)
    Artist_Nationality = models.CharField(max_length=254, null=True, blank=True)
    Artist_Begin_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_End_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_ULAN_URL = models.URLField(max_length=1024, null=True, blank=True)
    Artist_Wikidata_URL = models.URLField(max_length=1024, null=True, blank=True)
    Object_Date = models.CharField(max_length=254, null=True, blank=True)
    Object_Begin_Date = models.CharField(max_length=254, null=True, blank=True)
    Object_End_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_Begin_Date = models.CharField(max_length=254, null=True, blank=True)
    Artist_End_Date = models.CharField(max_length=254, null=True, blank=True)
    Medium = models.CharField(max_length=254, null=True, blank=True)
    Dimensions = models.URLField(max_length=1024, null=True, blank=True)
    Credit_Line = models.URLField(max_length=1024, null=True, blank=True)
    Classification = models.CharField(max_length=254, null=True, blank=True)
    Link_Resource = models.CharField(max_length=254, null=True, blank=True)
    Object_Wikidata_URL = models.URLField(max_length=1024, null=True, blank=True)
    Tags = models.CharField(max_length=254, null=True, blank=True)
    Tags_AAT_URL = models.CharField(max_length=254, null=True, blank=True)
    Tags_Wikidata_URL = models.URLField(max_length=1024, null=True, blank=True)


    def __str__(self):
        return self.name

# pk,model,name,Period,price,Artist_Display_Name,Artist_Display_Bio,Artist_Alpha_Sort,Artist_Nationality,Artist_Begin_Date,Artist_End_Date,Artist_ULAN_URL,Artist_Wikidata_URL,Object_Date,Object_Begin_Date,Object_End_Date,Medium,Dimensions,Credit_Line,Classification,Link_Resource,Object_Wikidata_URL,Tags,Tags_AAT_URL,Tags_Wikidata_URL