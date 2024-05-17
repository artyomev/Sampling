from django.db.models.signals import post_save
from django.dispatch import receiver
from analysis.models import AnalysisParameters
from analysis.utils import gen_random_seed


@receiver(post_save, sender=AnalysisParameters)
def generate_random_seed(**kwargs):
    instance = kwargs.get('instance')
    created = kwargs.get('created')
    if instance.generate_random_seed:
        if created:
            instance.random_seed = gen_random_seed()