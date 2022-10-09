from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Attendance(models.Model):
    """ store the attendance record """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_attendance')
    login_datetime = models.DateTimeField(auto_now_add=True)
    working = models.BooleanField()

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'tbl_attendance'
