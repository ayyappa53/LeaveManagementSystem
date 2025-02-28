# Generated by Django 4.1 on 2024-01-02 10:23

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("mble", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "gdr",
                    models.CharField(
                        choices=[
                            ("0", "--- Select Your Gender ---"),
                            ("1", "Male"),
                            ("2", "Female"),
                        ],
                        default="0",
                        max_length=5,
                    ),
                ),
                (
                    "role_type",
                    models.CharField(
                        choices=[("0", "Guest"), ("1", "Student"), ("2", "Teacher")],
                        default="0",
                        max_length=5,
                    ),
                ),
                ("eid", models.CharField(max_length=10)),
                ("pfimg", models.ImageField(default="pfle.png", upload_to="Profiles/")),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager()),],
        ),
        migrations.CreateModel(
            name="TchProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tchdesg", models.CharField(max_length=20)),
                ("tchexpr", models.IntegerField()),
                ("tchsubject", models.CharField(max_length=50)),
                ("tchbrnch", models.CharField(max_length=50)),
                ("tstatus", models.BooleanField(default=False)),
                (
                    "tc",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sbranch", models.CharField(max_length=50)),
                ("syear", models.CharField(max_length=50)),
                ("sstatus", models.BooleanField(default=False)),
                (
                    "sc",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Leave",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "leavetype",
                    models.CharField(
                        choices=[
                            ("s", "Select your Leave Type"),
                            ("Personal", "Personal"),
                            ("Medical", "Medical"),
                        ],
                        default="s",
                        max_length=15,
                    ),
                ),
                ("startdate", models.DateField()),
                ("enddate", models.DateField()),
                ("apldate", models.DateField(auto_now_add=True)),
                ("reason", models.CharField(max_length=200)),
                (
                    "leavestatus",
                    models.CharField(
                        choices=[
                            ("g", "Pending"),
                            ("a", "Approved"),
                            ("d", "Declined"),
                        ],
                        default="g",
                        max_length=10,
                    ),
                ),
                ("tchdesc", models.CharField(max_length=200)),
                ("leaatch", models.FileField(upload_to="Attachments/")),
                (
                    "st",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
