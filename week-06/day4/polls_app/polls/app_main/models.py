from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Poll(models.Model):
    pass

class Question(models.Model):
    description = models.TextField(null=False)

    def __str__(self):
        return f"ID: {self.id} Q: {self.description}"
    
    def __repr__(self):
        return f"ID: {self.id} Q: {self.description}"

class Response(models.Model):
    """
    Holds both the description of a Response option to a Question, and,
    the number of people who selected that Response.
    """
    description = models.TextField(null=False)
    number_of_responses = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, R: {self.description}, num_reponses: {self.number_of_responses}"