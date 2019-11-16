from itertools import combinations
from django.forms.models import model_to_dict

def combs(input):
    return sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])  

def model_to_dict_remove_id(model):
    result = model_to_dict(model)
    del result['id']
    return result
