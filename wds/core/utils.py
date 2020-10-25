from .models import traderequest


def get_trade_request_or_false(sender, receiver):
	try:
		return traderequest.objects.get(sender=sender, receiver=receiver, is_active=True)
	except traderequest.DoesNotExist:
		return False