# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountLogin(models.Model):
    login_attempt_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('UserAccount', models.DO_NOTHING, blank=True, null=True)
    user_account = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=100)
    ip_number = models.BigIntegerField(blank=True, null=True)
    browser_type = models.CharField(max_length=45, blank=True, null=True)
    success = models.CharField(max_length=1, blank=True, null=True)
    login_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_login'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ImageTags(models.Model):
    image = models.ForeignKey('Images', models.DO_NOTHING)
    tag = models.ForeignKey('Tags', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'image_tags'


class Images(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_url = models.TextField()
    business = models.ForeignKey('Listings', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class Listings(models.Model):
    business_id = models.BigAutoField(primary_key=True)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    business_website = models.CharField(max_length=200, blank=True, null=True)
    business_category = models.CharField(max_length=45)
    business_sm_id = models.BigIntegerField(blank=True, null=True)
    business_email_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    business_hours = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listings'


class ListingsBkp(models.Model):
    business_id = models.BigIntegerField(blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    business_website = models.CharField(max_length=200, blank=True, null=True)
    business_category = models.CharField(max_length=45, blank=True, null=True)
    business_sm_id = models.BigIntegerField(blank=True, null=True)
    business_email_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    business_hours = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listings_bkp'


class Location(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    business = models.ForeignKey(Listings, models.DO_NOTHING)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=50)
    phone = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class LocationBkp(models.Model):
    address_id = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    business_id = models.BigIntegerField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    phone = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_bkp'


class SocialMedia(models.Model):
    business_sm_id = models.BigAutoField(primary_key=True)
    business = models.ForeignKey(Listings, models.DO_NOTHING)
    fb_url = models.TextField(blank=True, null=True)
    ig_url = models.TextField(blank=True, null=True)
    tw_url = models.TextField(blank=True, null=True)
    other_url = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'social_media'


class Tags(models.Model):
    tag_id = models.BigIntegerField(primary_key=True)
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class UserAccount(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_account_name = models.CharField(unique=True, max_length=45)
    user_email = models.TextField(unique=True, blank=True, null=True)
    user_phone = models.BigIntegerField(unique=True)
    user_full_name = models.TextField(blank=True, null=True)
    business_user_flag = models.CharField(max_length=1)
    user_create_date = models.DateField()
    user_business = models.ForeignKey(Listings, models.DO_NOTHING, blank=True, null=True)
    user_active = models.CharField(max_length=1, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account'