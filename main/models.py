from django.db import models
from django.contrib.auth.models import User


# =========================
# SUBJECT MODEL
# =========================

class Subject(models.Model):

    name = models.CharField(
        max_length=100
    )

    teacher = models.CharField(
        max_length=100
    )

    total_weeks = models.IntegerField(
        default=15
    )

    def __str__(self):

        return self.name


# =========================
# STUDENT MODEL
# =========================

class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=100
    )

    group = models.CharField(
        max_length=50
    )

    phone = models.CharField(
        max_length=20
    )

    faculty = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    def __str__(self):

        return self.name


# =========================
# ATTENDANCE MODEL
# =========================

class Attendance(models.Model):

    STATUS = (

        ('present', '✅ Keldi'),

        ('late', '🕒 Kechikdi'),

        ('excused', '📄 Sababli kelmadi'),

        ('absent', '❌ Sababsiz kelmadi'),

    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    week = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    late_minutes = models.IntegerField(
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    reason = models.TextField(
        blank=True,
        null=True
    )

    class Meta:

        unique_together = (
            'student',
            'subject',
            'week'
        )

    def __str__(self):

        return (
            f"{self.student.name} - "
            f"{self.subject.name}"
        )
    class Meta:

        unique_together = (
            'student',
            'subject',
            'week'
        )

    # DATE + TIME
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # LATE MINUTES
    late_minutes = models.IntegerField(
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    reason = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return (
            f"{self.student.name} - "
            f"{self.subject.name}"
        )

    class Meta:

        unique_together = (
            'student',
            'subject',
            'week'
        )

    # DATE + TIME
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # LATE MINUTES
    late_minutes = models.IntegerField(
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    reason = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return (
            f"{self.student.name} - "
            f"{self.subject.name}"
        )