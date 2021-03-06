# Generated by Django 3.2.6 on 2021-08-20 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('first_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('change_message', models.TextField()),
                ('action_flag', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            name='Education',
            fields=[
                ('id', models.IntegerField(blank=True, db_column='ID', primary_key=True, serialize=False)),
                ('org_id', models.TextField(blank=True, null=True)),
                ('org_name', models.TextField(blank=True, null=True)),
                ('user_id', models.TextField(blank=True, null=True)),
                ('student_name', models.TextField(blank=True, db_column='Student_Name', null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('first_name', models.TextField(blank=True, null=True)),
                ('middle_name', models.TextField(blank=True, null=True)),
                ('last_name', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('user_student_id', models.TextField(blank=True, null=True)),
                ('degree_ordinal', models.IntegerField(blank=True, null=True)),
                ('education_level', models.TextField(blank=True, db_column='Education_Level', null=True)),
                ('degree_name', models.TextField(blank=True, null=True)),
                ('field_of_study', models.TextField(blank=True, null=True)),
                ('field_of_study_description', models.TextField(blank=True, null=True)),
                ('school_name', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('state_name', models.TextField(blank=True, null=True)),
                ('country_name', models.TextField(blank=True, null=True)),
                ('degree_start_month', models.TextField(blank=True, null=True)),
                ('degree_start_year', models.TextField(blank=True, null=True)),
                ('degree_completion_month', models.TextField(blank=True, null=True)),
                ('degree_completion_year', models.TextField(blank=True, null=True)),
                ('degree_in_progress', models.TextField(blank=True, null=True)),
                ('anticipated_graduation_month', models.TextField(blank=True, null=True)),
                ('anticipated_graduation_year', models.TextField(blank=True, null=True)),
                ('verified', models.TextField(blank=True, null=True)),
                ('verified_by_user', models.TextField(blank=True, null=True)),
                ('job_category_name', models.TextField(blank=True, null=True)),
                ('job_category_id', models.IntegerField(blank=True, null=True)),
                ('update_datetime', models.TextField(blank=True, null=True)),
                ('dept_node_id', models.TextField(blank=True, db_column='Dept_Node_ID', null=True)),
                ('dept_name', models.TextField(blank=True, db_column='Dept_Name', null=True)),
                ('facility_node_id', models.TextField(blank=True, db_column='Facility_node_id', null=True)),
                ('facility_name', models.TextField(blank=True, db_column='Facility_Name', null=True)),
                ('is_published', models.IntegerField(blank=True, db_column='Is_Published', null=True)),
                ('is_preceptor', models.IntegerField(blank=True, db_column='Is_Preceptor', null=True)),
                ('is_certified', models.IntegerField(blank=True, db_column='Is_Certified', null=True)),
                ('is_supervisor', models.TextField(blank=True, null=True)),
                ('supervisor_user_id', models.TextField(blank=True, null=True)),
                ('supervisor_first_name', models.TextField(blank=True, null=True)),
                ('supervisor_middle_name', models.TextField(blank=True, null=True)),
                ('supervisor_last_name', models.TextField(blank=True, null=True)),
                ('supervisor_email', models.TextField(blank=True, null=True)),
                ('anticipated_graduation_year_customsqlquery_field', models.TextField(blank=True, db_column='anticipated_graduation_year(CustomSQLQuery)', null=True)),
                ('e_year_distr', models.TextField(blank=True, null=True)),
                ('y_year_distr', models.TextField(blank=True, null=True)),
                ('year_distr_order', models.TextField(blank=True, null=True)),
                ('lvl1_id', models.TextField(blank=True, db_column='Lvl1_ID', null=True)),
                ('lvl2_id', models.TextField(blank=True, db_column='Lvl2_ID', null=True)),
                ('lvl3_id', models.TextField(blank=True, db_column='Lvl3_ID', null=True)),
                ('lvl4_id', models.TextField(blank=True, db_column='Lvl4_ID', null=True)),
                ('lvl5_id', models.TextField(blank=True, db_column='Lvl5_ID', null=True)),
                ('lvl6_id', models.TextField(blank=True, db_column='Lvl6_ID', null=True)),
                ('lvl7_id', models.TextField(blank=True, db_column='Lvl7_ID', null=True)),
                ('lvl8_id', models.TextField(blank=True, db_column='Lvl8_ID', null=True)),
                ('lvl9_id', models.TextField(blank=True, db_column='Lvl9_ID', null=True)),
                ('level1', models.TextField(blank=True, db_column='Level1', null=True)),
                ('level2', models.TextField(blank=True, db_column='Level2', null=True)),
                ('level3', models.TextField(blank=True, db_column='Level3', null=True)),
                ('level4', models.TextField(blank=True, db_column='Level4', null=True)),
                ('level5', models.TextField(blank=True, db_column='Level5', null=True)),
                ('level6', models.TextField(blank=True, db_column='Level6', null=True)),
                ('level7', models.TextField(blank=True, db_column='Level7', null=True)),
                ('level8', models.TextField(blank=True, db_column='Level8', null=True)),
                ('level9', models.TextField(blank=True, db_column='Level9', null=True)),
                ('org_node_id', models.TextField(blank=True, db_column='Org_Node_id', null=True)),
                ('org_node_name', models.TextField(blank=True, db_column='Org_Node_Name', null=True)),
                ('org_name1', models.TextField(blank=True, db_column='Org_Name1', null=True)),
                ('org_id1', models.TextField(blank=True, db_column='Org_Id1', null=True)),
                ('org_node_type', models.FloatField(blank=True, db_column='Org_Node_Type', null=True)),
            ],
            options={
                'db_table': 'Education',
                'managed': False,
            },
        ),
    ]
