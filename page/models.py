from __future__ import unicode_literals

from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class Post(models.Model):
    description = models.CharField(verbose_name=_("Description"), max_length=100)
    photo = models.ImageField(verbose_name=_("Photo"), null=True, blank=True)
    owner = models.ForeignKey(verbose_name=_("Owner"), to='MyUser', related_name="posts")
    created = models.DateTimeField(verbose_name=_("Created"), auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return "{} - {}".format(self.owner.email, self.description)


class Vote(models.Model):
    vote = models.BooleanField(verbose_name=_("Vote"))
    post = models.ForeignKey("Post", related_name="vote")
    user = models.ForeignKey("MyUser", related_name="vote")
    date = models.DateField(verbose_name=_("Data dodania"), auto_now=True)


# class Notify(models.Model):
#     type = models.IntegerField()


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        unique=True,
    )
    nick = models.CharField(
        verbose_name=_("Nick"),
        max_length=100,
        null=True,
        blank=True,
        unique=True
    )
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=100,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=100,
        null=True,
        blank=True
    )

    avatar = models.ImageField(verbose_name=_("Avatar"), blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_name(self):
        if self.first_name and self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        else:
            if self.first_name:
                return self.first_name
            if self.last_name:
                return self.last_name

        if self.nick:
            return self.nick

        return self.email
