from django.db import models
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class LandingPage(models.Model):
    email = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=100, blank=True)
    variation = models.CharField(max_length=10, blank=True)
    level = models.CharField(max_length=100, blank=True)

    comment = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.email


class LandingForm(ModelForm):
    class Meta:
        model = LandingPage
        fields = ('email', )


class ContributeForm(ModelForm):
    class Meta:
        model = LandingPage
        fields = ('name', 'email', 'comment', )

        widgets = {
            'comment': Textarea(attrs={'cols': 80, 'rows': 10}),
        }


###########  Extend user profile
# Docs: http://stackoverflow.com/a/965883/705945

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)
###########  Extend user profile  - END
