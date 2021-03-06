# Generated by Django 3.1.7 on 2021-05-16 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountLogin',
            fields=[
                ('login_attempt_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_account', models.CharField(blank=True, max_length=45, null=True)),
                ('password', models.CharField(max_length=100)),
                ('ip_number', models.BigIntegerField(blank=True, null=True)),
                ('browser_type', models.CharField(blank=True, max_length=45, null=True)),
                ('success', models.CharField(blank=True, max_length=1, null=True)),
                ('login_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'account_login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('image_url', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ImageTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'image_tags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('business_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('business_name', models.CharField(blank=True, max_length=100, null=True)),
                ('business_website', models.CharField(blank=True, max_length=200, null=True)),
                ('business_category', models.CharField(max_length=45)),
                ('business_sm_id', models.BigIntegerField(blank=True, null=True)),
                ('business_email_id', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('business_hours', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'listings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListingsBkp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.BigIntegerField(blank=True, null=True)),
                ('business_name', models.CharField(blank=True, max_length=100, null=True)),
                ('business_website', models.CharField(blank=True, max_length=200, null=True)),
                ('business_category', models.CharField(blank=True, max_length=45, null=True)),
                ('business_sm_id', models.BigIntegerField(blank=True, null=True)),
                ('business_email_id', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('business_hours', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'listings_bkp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('address_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=10)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocationBkp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.BigIntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('business_id', models.BigIntegerField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'location_bkp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('business_sm_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fb_url', models.TextField(blank=True, null=True)),
                ('ig_url', models.TextField(blank=True, null=True)),
                ('tw_url', models.TextField(blank=True, null=True)),
                ('other_url', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'social_media',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tags', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tags',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_account_name', models.CharField(max_length=45, unique=True)),
                ('user_email', models.TextField(blank=True, null=True, unique=True)),
                ('user_phone', models.BigIntegerField(unique=True)),
                ('user_full_name', models.TextField(blank=True, null=True)),
                ('business_user_flag', models.CharField(max_length=1)),
                ('user_create_date', models.DateField()),
                ('user_active', models.CharField(blank=True, max_length=1, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'user_account',
                'managed': False,
            },
        ),
    ]
