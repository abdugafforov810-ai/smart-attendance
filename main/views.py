from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from reportlab.pdfgen import canvas
import qrcode
import requests

from .models import (
    Student,
    Subject,
    Attendance
)


# =========================
# TELEGRAM BOT
# =========================

TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"


# =========================
# LOGIN
# =========================

def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect('/')

    return render(
        request,
        'main/login.html'
    )


# =========================
# LOGOUT
# =========================

@login_required
def logout_view(request):

    logout(request)

    return redirect('/login/')


# =========================
# DASHBOARD
# =========================

@login_required
def dashboard(request):

    students_count = Student.objects.count()

    subjects_count = Subject.objects.count()

    attendance_count = Attendance.objects.count()

    present_count = Attendance.objects.filter(
        status='present'
    ).count()

    late_count = Attendance.objects.filter(
        status='late'
    ).count()

    absent_count = Attendance.objects.filter(
        status='absent'
    ).count()

    excused_count = Attendance.objects.filter(
        status='excused'
    ).count()

    percent = 0

    if attendance_count > 0:

        percent = round(
            (
                (present_count + late_count)
                / attendance_count
            ) * 100,
            1
        )

    students = Student.objects.all()

    student_data = []

    for student in students:

        total = Attendance.objects.filter(
            student=student
        ).count()

        present = Attendance.objects.filter(
            student=student,
            status__in=['present', 'late']
        ).count()

        absent = Attendance.objects.filter(
            student=student,
            status='absent'
        ).count()

        excused = Attendance.objects.filter(
            student=student,
            status='excused'
        ).count()

        score = (
            (present * 5)
            +
            (excused * 1)
            -
            (absent * 5)
        )

        percent_student = 0

        if total > 0:

            percent_student = round(
                (present / total) * 100,
                1
            )

        if percent_student >= 90:

            student_status = "🏆 Excellent"

        elif percent_student >= 75:

            student_status = "✅ Good"

        elif percent_student >= 50:

            student_status = "⚠️ Warning"

        elif percent_student >= 30:

            student_status = "🚨 Risk"

        else:

            student_status = "❌ FAIL"

        if percent_student >= 50:

            exam_access = "✅ Ruxsat"

        else:

            exam_access = "🚫 Taqiqlangan"

        student_data.append({

            'name': student.name,
            'group': student.group,

            'present': present,
            'absent': absent,
            'excused': excused,

            'score': score,

            'percent': percent_student,

            'student_status': student_status,

            'exam_access': exam_access,

        })

    context = {

        'students_count': students_count,
        'subjects_count': subjects_count,
        'attendance_count': attendance_count,

        'present_count': present_count,
        'late_count': late_count,
        'absent_count': absent_count,
        'excused_count': excused_count,

        'percent': percent,

        'student_data': student_data,

    }

    return render(
        request,
        'main/dashboard.html',
        context
    )


# =========================
# QR CODE
# =========================

@login_required
def generate_qr(request):

    qr = qrcode.make(
        "http://127.0.0.1:8000/attendance/"
    )

    response = HttpResponse(
        content_type="image/png"
    )

    qr.save(response, "PNG")

    return response


# =========================
# ATTENDANCE
# =========================

@login_required
def mark_attendance(request):

    students = Student.objects.all()

    subjects = Subject.objects.all()

    if request.method == 'POST':

        student_id = request.POST.get('student')

        subject_id = request.POST.get('subject')

        week = request.POST.get('week')

        status = request.POST.get('status')

        reason = request.POST.get('reason')

        student = Student.objects.get(
            id=student_id
        )

        subject = Subject.objects.get(
            id=subject_id
        )

        # DUPLICATE CHECK
        existing = Attendance.objects.filter(
            student=student,
            subject=subject,
            week=week
        ).exists()

        if existing:

            return HttpResponse(
                "Attendance already exists!"
            )

        # SAVE
        attendance = Attendance.objects.create(

            student=student,
            subject=subject,
            week=week,
            status=status,
            reason=reason

        )

        # STATUS TEXT
        status_text = {

            'present': '✅ Keldi',
            'late': '🕒 Kechikdi',
            'excused': '📄 Sababli kelmadi',
            'absent': '❌ Sababsiz kelmadi'

        }.get(status, status)

        # TELEGRAM MESSAGE
        message = f'''
📢 Yangi davomat

👨‍🎓 Student: {student.name}
📚 Fan: {subject.name}
📅 Hafta: {week}
📌 Holat: {status_text}
⏰ Vaqt: {attendance.created_at.strftime("%d.%m.%Y | %H:%M")}
'''

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        data = {

            "chat_id": CHAT_ID,
            "text": message

        }

        requests.post(url, data=data)

        return redirect('/attendance/')

    return render(
        request,
        'main/attendance.html',
        {
            'students': students,
            'subjects': subjects
        }
    )


# =========================
# PDF EXPORT
# =========================

@login_required
def export_pdf(request):

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="attendance.pdf"'
    )

    p = canvas.Canvas(response)

    p.setFont(
        "Helvetica-Bold",
        18
    )

    p.drawString(
        180,
        820,
        "Attendance Report"
    )

    p.setFont(
        "Helvetica",
        12
    )

    y = 760

    for student in Student.objects.all():

        p.drawString(
            100,
            y,
            f"Student: {student.name}"
        )

        y -= 30

    p.save()

    return response