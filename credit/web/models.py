from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


GENDER_CHOICES = {
    ('man', '남자'),
    ('woman', '여자'),
}

ANSWER_CHOICES = {
    ('yes', '예'),
    ('no', '아니오'),
}

HOUSE_CHOICES = {
    ('monthly', '월세'),
    ('charter', '전세'),
    ('hold', '본인명의'),
    ('family_hold', '가족명의')
}

DATE_CHOICES = {
    ('daily', '일수'),
    ('monthly', '월상품'),
    ('weekly', '주상품'),
}

MARRY_CHOICES = {
    ('marry', '기혼'),
    ('not_marry', '미혼'),
    ('miss_marry', '이혼'),
}

CHILD_CHOICES = {
    ('not_child', '자녀없음'),
    ('raise_child', '있음(육아)'),
    ('not_raise_child', '있음(육아안함)'),
}



class Form(models.Model):
    id = models.AutoField(primary_key=True)

    date = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=40, verbose_name="이름")

    phone_number = models.CharField(max_length=40, verbose_name="휴대폰번호")

    region = models.CharField(max_length=400, verbose_name="지역")

    age = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ], verbose_name="나이")

    gender = models.CharField(max_length=40, choices=GENDER_CHOICES, verbose_name="성별")

    job = models.CharField(null=True, blank=True, max_length=400, verbose_name="직업")

    pay = models.IntegerField(validators=[
            MaxValueValidator(100000000),
            MinValueValidator(0)
        ], verbose_name="급여(만원)")

    pay_day = models.IntegerField(validators=[
            MaxValueValidator(99),
            MinValueValidator(1)
        ], verbose_name="급여날짜(일)")

    use_bool = models.CharField(max_length=40, choices=ANSWER_CHOICES, verbose_name="개인돈사용여부")
    use_ps = models.TextField(max_length=4000, null=True, blank=True, verbose_name="개인돈사용내역")

    credit_grade = models.IntegerField(validators=[
            MaxValueValidator(9999),
            MinValueValidator(0)
        ], verbose_name="신용점수")

    holding_credit = models.IntegerField(null=True, blank=True,validators=[
            MaxValueValidator(1000000),
            MinValueValidator(0)
        ], verbose_name="기대출(만원)")

    holding_house = models.CharField(max_length=40, choices=HOUSE_CHOICES, verbose_name="주거형태")

    holding_car = models.CharField(max_length=40, choices=ANSWER_CHOICES, verbose_name="자차소유")

    credit_amount = models.IntegerField(validators=[
            MaxValueValidator(100000000),
            MinValueValidator(1)
        ], verbose_name="대출신청금(만원)")

    credit_date = models.CharField(null=True,blank=True,max_length=40, choices=DATE_CHOICES, verbose_name="원하는상환방식")

    is_married = models.CharField(max_length=40, choices=MARRY_CHOICES, verbose_name="결혼여부")

    is_child = models.CharField(max_length=40, choices=CHILD_CHOICES, verbose_name="자녀여부")


    def __str__(self):
        return '(' + str(self.pk) + ') ' + str(self.date) + ' / ' +self.name + ' / ' + str(self.age) + '세 / ' + self.region

    class Meta:
        db_table = 'forms'
        verbose_name = '신청서'
        verbose_name_plural = '신청서'

class User(models.Model):
    user_id = models.CharField(unique=True, max_length=50, verbose_name="아이디")
    user_pw = models.CharField(max_length=200, verbose_name="비밀번호")

    def __str__(self):
        return str(self.user_id + ' / ' + self.user_pw)

    class Meta:
        db_table = 'users'
        verbose_name = '유저'
        verbose_name_plural = '유저'
