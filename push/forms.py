from django import forms
from .models import SubscriptionInfo


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = SubscriptionInfo
        fields = ('endpoint', 'auth', 'p256dh', 'browser')

    def save(self):
        data = self.cleaned_data
        SubscriptionInfo.objects.all().delete()
        subscription = SubscriptionInfo.objects.create(**data)
        return subscription

    @classmethod
    def process_subscription_data(cls, post_data):
        """Process the subscription data according to our model"""
        subscription_data = post_data.pop("subscription", {})
        # As our database saves the auth and p256dh key in separate field,
        # we need to refactor it and insert the auth and p256dh keys in the same dictionary
        keys = subscription_data.pop("keys", {})
        subscription_data.update(keys)
        # Insert the browser name
        subscription_data["browser"] = post_data.pop("browser")

        return subscription_data
