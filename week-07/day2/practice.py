from django.db import models
from django.db.models import Q

class Companies(models.Model):
      name = models.CharField(max_length = 250)
     
amazon = Companies('amazon')
web = Companies('web')
services = Companies('services') 
facebook = Companies('facebook')

possible_merchants = ["amazon", "web", "services"]

def companies_matching(merchants):
    q = Q()
    for merchant in merchants:
            q |= Q(name__icontains = merchant)
    return Companies.objects.filter(q)