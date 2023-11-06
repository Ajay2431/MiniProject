from .models import BatchUserMapping
def get_batch(username):
    batch_qs=BatchUserMapping.objects.filter(username=username)
    for batch in batch_qs:
        return batch.name
    return ""
