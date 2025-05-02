from django.db import models

from django.contrib import admin

class bankloan(models.Model):
    Loan_ID=models.IntegerField(primary_key=True)
    Loan_Type=models.CharField(max_length=30)
    Loan_Amt=models.IntegerField()
    cust_accno=models.IntegerField()
    cust_name=models.CharField(max_length=30)

class bankloanAdmin(admin.ModelAdmin):
    list_display=('Loan_ID','Loan_Type','Loan_Amt','cust_accno','cust_name')