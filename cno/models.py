# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Education(models.Model):
    id = models.IntegerField(db_column='ID', blank=False, null=False, primary_key=True)  # Field name made lowercase.
    org_id = models.TextField(blank=True, null=True)
    org_name = models.TextField(blank=True, null=True)
    user_id = models.TextField(blank=True, null=True)
    student_name = models.TextField(db_column='Student_Name', blank=True, null=True)  # Field name made lowercase.
    username = models.IntegerField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    middle_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    user_student_id = models.TextField(blank=True, null=True)
    degree_ordinal = models.IntegerField(blank=True, null=True)
    education_level = models.TextField(db_column='Education_Level', blank=True, null=True)  # Field name made lowercase.
    degree_name = models.TextField(blank=True, null=True)
    field_of_study = models.TextField(blank=True, null=True)
    field_of_study_description = models.TextField(blank=True, null=True)
    school_name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    country_name = models.TextField(blank=True, null=True)
    degree_start_month = models.TextField(blank=True, null=True)
    degree_start_year = models.TextField(blank=True, null=True)
    degree_completion_month = models.TextField(blank=True, null=True)
    degree_completion_year = models.TextField(blank=True, null=True)
    degree_in_progress = models.TextField(blank=True, null=True)
    anticipated_graduation_month = models.TextField(blank=True, null=True)
    anticipated_graduation_year = models.TextField(blank=True, null=True)
    verified = models.TextField(blank=True, null=True)
    verified_by_user = models.TextField(blank=True, null=True)
    job_category_name = models.TextField(blank=True, null=True)
    job_category_id = models.IntegerField(blank=True, null=True)
    update_datetime = models.TextField(blank=True, null=True)
    dept_node_id = models.TextField(db_column='Dept_Node_ID', blank=True, null=True)  # Field name made lowercase.
    dept_name = models.TextField(db_column='Dept_Name', blank=True, null=True)  # Field name made lowercase.
    facility_node_id = models.TextField(db_column='Facility_node_id', blank=True, null=True)  # Field name made lowercase.
    facility_name = models.TextField(db_column='Facility_Name', blank=True, null=True)  # Field name made lowercase.
    is_published = models.IntegerField(db_column='Is_Published', blank=True, null=True)  # Field name made lowercase.
    is_preceptor = models.IntegerField(db_column='Is_Preceptor', blank=True, null=True)  # Field name made lowercase.
    is_certified = models.IntegerField(db_column='Is_Certified', blank=True, null=True)  # Field name made lowercase.
    is_supervisor = models.TextField(blank=True, null=True)
    supervisor_user_id = models.TextField(blank=True, null=True)
    supervisor_first_name = models.TextField(blank=True, null=True)
    supervisor_middle_name = models.TextField(blank=True, null=True)
    supervisor_last_name = models.TextField(blank=True, null=True)
    supervisor_email = models.TextField(blank=True, null=True)
    anticipated_graduation_year_customsqlquery_field = models.TextField(db_column='anticipated_graduation_year(CustomSQLQuery)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    e_year_distr = models.TextField(blank=True, null=True)
    y_year_distr = models.TextField(blank=True, null=True)
    year_distr_order = models.TextField(blank=True, null=True)
    lvl1_id = models.TextField(db_column='Lvl1_ID', blank=True, null=True)  # Field name made lowercase.
    lvl2_id = models.TextField(db_column='Lvl2_ID', blank=True, null=True)  # Field name made lowercase.
    lvl3_id = models.TextField(db_column='Lvl3_ID', blank=True, null=True)  # Field name made lowercase.
    lvl4_id = models.TextField(db_column='Lvl4_ID', blank=True, null=True)  # Field name made lowercase.
    lvl5_id = models.TextField(db_column='Lvl5_ID', blank=True, null=True)  # Field name made lowercase.
    lvl6_id = models.TextField(db_column='Lvl6_ID', blank=True, null=True)  # Field name made lowercase.
    lvl7_id = models.TextField(db_column='Lvl7_ID', blank=True, null=True)  # Field name made lowercase.
    lvl8_id = models.TextField(db_column='Lvl8_ID', blank=True, null=True)  # Field name made lowercase.
    lvl9_id = models.TextField(db_column='Lvl9_ID', blank=True, null=True)  # Field name made lowercase.
    level1 = models.TextField(db_column='Level1', blank=True, null=True)  # Field name made lowercase.
    level2 = models.TextField(db_column='Level2', blank=True, null=True)  # Field name made lowercase.
    level3 = models.TextField(db_column='Level3', blank=True, null=True)  # Field name made lowercase.
    level4 = models.TextField(db_column='Level4', blank=True, null=True)  # Field name made lowercase.
    level5 = models.TextField(db_column='Level5', blank=True, null=True)  # Field name made lowercase.
    level6 = models.TextField(db_column='Level6', blank=True, null=True)  # Field name made lowercase.
    level7 = models.TextField(db_column='Level7', blank=True, null=True)  # Field name made lowercase.
    level8 = models.TextField(db_column='Level8', blank=True, null=True)  # Field name made lowercase.
    level9 = models.TextField(db_column='Level9', blank=True, null=True)  # Field name made lowercase.
    org_node_id = models.TextField(db_column='Org_Node_id', blank=True, null=True)  # Field name made lowercase.
    org_node_name = models.TextField(db_column='Org_Node_Name', blank=True, null=True)  # Field name made lowercase.
    org_name1 = models.TextField(db_column='Org_Name1', blank=True, null=True)  # Field name made lowercase.
    org_id1 = models.TextField(db_column='Org_Id1', blank=True, null=True)  # Field name made lowercase.
    org_node_type = models.IntegerField(db_column='Org_Node_Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Education'
