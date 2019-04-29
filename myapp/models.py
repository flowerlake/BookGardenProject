from django.db import models


# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=17, blank=True)
    book_name = models.CharField(max_length=64)
    book_num = models.IntegerField(default=1)

    def __str__(self):
        return self.book_name


class Book_loan(models.Model):
    user_id = models.CharField(max_length=10, null=True)
    book_name = models.CharField(max_length=64, null=True)
    add_time = models.DateTimeField(null=True)
    return_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.user_id


class Book_loan_copy(models.Model):
    user_id = models.CharField(max_length=10, null=True)
    book_name = models.CharField(max_length=64, null=True)
    add_time = models.DateTimeField(null=True)
    return_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.user_id


class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    user_name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.EmailField(null=True)

    user_qd = models.IntegerField()
    user_class = models.IntegerField()
    dorm_num = models.CharField(max_length=3)
    is_authenticated = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id


class Sta_fkm(models.Model):
    # 分别为五公里、引体向上、仰卧起坐、俯卧撑
    user_id = models.CharField(max_length=10, null=True)
    five_km = models.TimeField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id + "---" + str(self.five_km)


class Sta_chining2(models.Model):
    # 分别为五公里、引体向上、仰卧起坐、俯卧撑
    user_id = models.CharField(max_length=10, null=True)
    chining = models.IntegerField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id + "---" + str(self.chining)


class Sta_sit2(models.Model):
    # 分别为五公里、引体向上、仰卧起坐、俯卧撑
    user_id = models.CharField(max_length=10, null=True)
    sit_up = models.IntegerField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id + "---" + str(self.sit_up)


class Sta_push2(models.Model):
    # 分别为五公里、引体向上、仰卧起坐、俯卧撑
    user_id = models.CharField(max_length=10, null=True)
    push_up = models.IntegerField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id


class grade(models.Model):
    # 学期
    user_id = models.CharField(max_length=10, primary_key=True)
    semester = models.CharField(max_length=64)


class sleep_status(models.Model):
    time_rating = models.FloatField()
    time = models.DateField()

    def __str__(self):
        return self.time_rating
