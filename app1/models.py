from django.db import models

# Create your models here.

class course(models.Model):
    cname = models.CharField(max_length=25)
    fee = models.IntegerField()    
    dur = models.IntegerField()
    trainer = models.CharField(max_length=25)


#Models are Python classes that define the structure of your database tables
#Models define the structure and fields of database tables. Each model class corresponds
# to a table in the database, and each field in the model represents a column in the table. 
#This allows you to create, read, update, and delete records in the database using Python code.
#Models are a crucial part of this ORM, as they define the mapping between Python objects and database tables.
#
