from django.contrib import admin
from myapp.models import Book, User, grade, Sta_fkm, Sta_chining2, Sta_push2, Sta_sit2, sleep_status, Book_loan, \
    Book_loan_copy

# Register your models here.
admin.site.register(Book)
admin.site.register(Book_loan)
admin.site.register(Book_loan_copy)
admin.site.register(User)
admin.site.register(Sta_fkm)
admin.site.register(Sta_chining2)
admin.site.register(Sta_push2)
admin.site.register(Sta_sit2)
admin.site.register(grade)
admin.site.register(sleep_status)
