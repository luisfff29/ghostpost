import random
import string


def order_posts(data, model_name):
    if data['order_by'] == 'date':
        result = model_name.objects.order_by('date')
    elif data['order_by'] == 'all_boasts':
        result = model_name.objects.order_by(
            'date').filter(boast_or_roast=True)
    elif data['order_by'] == 'all_roasts':
        result = model_name.objects.order_by(
            'date').filter(boast_or_roast=False)
    elif data['order_by'] == 'up_vote':
        result = model_name.objects.order_by('-up_vote', 'date')
    elif data['order_by'] == 'down_vote':
        result = model_name.objects.order_by('-down_vote', 'date')
    elif data['order_by'] == 'vote_difference':
        result = model_name.objects.extra(
            select={'diff': 'up_vote - down_vote'}).order_by('-diff')
    return result


def get_magic_str():
    str_plus_nums = string.ascii_letters + string.digits
    return ''.join((random.choice(str_plus_nums) for x in range(6)))
