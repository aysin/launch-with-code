from django.db import models

# Create your models here.
class Join(models.Model):
	ip_address = models.CharField(max_length=120, default='ABC')
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return "%s" %(self.email)

# 1. install south: pip install south, add south to settings.py 
# 2. Ensure your models is in the database
# 3. Convert the model to south with python manage.py convert_to_south appname
# 4. Make changes to model
# 5. Run schemamigration with pyhton manage.py schemamigration appname --auto
# 6. Run migrate python manage.py migrate