from django.db import models

class Dream(models.Model):
	CATEGORY_CHOICES = (
	    ('colours', 'Colours'),
	    ('relations', 'Relations'),
	    ('churches', 'Churches'),
	    ('cities', 'Cities'),
	    ('subjects', 'Subjects'),
	    ('vehicle', 'Vehicle'),
	    ('food', 'Food'),
	    ('fruits', 'Fruits'),
	    ('animal', 'Animal'),
	    ('places', 'Places'),
	    ('activities', 'Activities'),
	    ('things', 'Things'),
  	)
	dream_name = models.CharField(max_length=100)
	meaning = models.TextField()
	category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

	def __str__(self):
		return str(self.dream_name)
