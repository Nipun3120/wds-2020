from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from notifications.models import Notification
from django.dispatch import receiver
# Create your models here.
stock_list=(
    ('stock1','stock1'),
    ('stock2','stock2'),
    ('stock3','stock3'),
    ('stock4','stock4'),
    ('stock5','stock5'),
    ('stock6','stock6'),
    ('stock7','stock7'),
    ('stock8','stock8'),
    ('stock9','stock9'),
    ('stock10','stock10'),
)

class Stock(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    stock1=models.IntegerField(default=0)
    stock2=models.IntegerField(default=0)
    stock3=models.IntegerField(default=0)
    stock4=models.IntegerField(default=0)
    stock5=models.IntegerField(default=0)
    stock6=models.IntegerField(default=0)
    stock7=models.IntegerField(default=0)
    stock8=models.IntegerField(default=0)
    stock9=models.IntegerField(default=0)
    stock10=models.IntegerField(default=0)
    userbalance=models.FloatField(default=1000000.0)
    def __str__(self):
        return f"{self.user}"
class trade(models.Model):
    seller=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stock=models.CharField(choices=stock_list,max_length=100)
    numberofstocks=models.IntegerField(default=0)
    priceperstock=models.FloatField(null=True, blank=True)
    buyer=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='buyer_of_stock', on_delete=models.CASCADE)
    #userbalance=models.FloatField(default=1000000.0)
    

def create_stock(sender,instance,created,**kwargs):
    if created:
        Stock.objects.create(user=instance)

post_save.connect(create_stock,sender=User)

class TradeList(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    traderequesthistoryitem=models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="traderequesthistoryitem")

    notifications = GenericRelation(Notification) 

    def __str__(self):
        return self.user.username

    def add_trade_history(self, other_trader):
        if not other_trader in self.traderequesthistoryitem.all():
            self.traderequesthistoryitem.add(other_trader)
            content_type = ContentType.objects.get_for_model(self)


            #Notification Creation
            self.notifications.create(
                target = self.user,
                from_user = other_trader,
                redirect_url = f"{settings.BASE_URL}/notifications.html/",
                verb=f"Request successfull with {other_trader.username}",
                content_type = content_type,
            )    
            self.save()



class traderequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name ="receiver")
    is_active = models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
        return self.sender

    def accept(self):
        receiver_trade_list = TradeList.objects.get(user=self.receiver)
        if(receiver_trade_list):
            content_type = ContentType.objects.get_for_model(self)
			# Update notification for RECEIVER
            receiver_notification = Notification.objects.get(target=self.receiver, content_type=content_type, object_id=self.id)
            receiver_notification.is_active = False
            receiver_notification.redirect_url = f"{settings.BASE_URL}/notifications.html/"
            receiver_notification.verb = f"You accepted {self.sender.username}'s Trade request."
            #receiver_notification.timestamp = timezone.now()
            receiver_notification.save()
            receiver_trade_list.add_trade_history(self.sender)
            # receiver_friend_list.save()
            sender_trade_list = TradeList.objects.get(user=self.sender)
            if sender_trade_list:

				# Create notification for SENDER
                self.notifications.create(
					target=self.sender,
					from_user=self.receiver,
					redirect_url=f"{settings.BASE_URL}/notifications.html/",
					verb=f"{self.receiver.username} accepted your Trade request.",
					content_type=content_type,
				)
                sender_trade_list.add_trade_history(self.receiver)
                # sender_friend_list.save()
                self.is_active = False
                self.save()
            return receiver_notification
			
    def decline(self):
        self.is_active = False
        self.save()
        content_type = ContentType.objects.get_for_model(self)
        # Update notification for RECEIVER
        notification = Notification.objects.get(target=self.receiver, content_type=content_type, object_id=self.id)
        notification.is_active = False
        notification.redirect_url = f"{settings.BASE_URL}/notifications.html/"
        notification.verb = f"You declined {self.sender}'s Trade request."
        notification.from_user = self.sender
        #notification.timestamp = timezone.now()
        notification.save()

		# Create notification for SENDER
        self.notifications.create(
			target=self.sender,
			verb=f"{self.receiver.username}'s Trade request declined.",
			from_user=self.receiver,
			redirect_url=f"{settings.BASE_URL}/notifications.html/",
			content_type=content_type,
        )
        return notification
        
@receiver(post_save, sender=traderequest)
def create_notification(sender, instance, created, **kwargs):
	if created:
		instance.notifications.create(
			target=instance.receiver,
			from_user=instance.sender,
			redirect_url=f"{settings.BASE_URL}/notifications.html/",
			verb=f"{instance.sender.username} sent you a Trade request.",
			content_type=instance,
		)
