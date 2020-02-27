from django.db import models


# Create your models here.
class AreaInfo(models.Model):
    """
    地区基本信息
    因为最细精确到街道，所以社区的内容被我删除了
    """
    name = models.CharField(max_length=30)  # 名称，长度为30是为了防止有些地名特别长
    identifier = models.CharField(max_length=10, unique=True)  # 标识符，用于自关联


class PersonInfo(models.Model):
    """人员登记信息"""
    # 审核状态
    # pending_choices = (
    #     ("pen", "等待审核"),
    #     ("pas", "通过"),
    #     ("rej", "未通过"),
    # )
    #
    # pending = models.CharField(max_length=3, choices=pending_choices)

    # 人员信息
    name = models.CharField(max_length=30)
    is_male = models.BooleanField()  # 性别，用 is_male 来代替

    id_type_choices = (
        ("idc", "身份证"),  # identity card
        ("mil", "军官证"),  # military card
        ("pas", "护照"),  # passport
        ("hmt", "港澳台通行证"),  # HongKong Macau and  Taiwan
        ("chi", "儿童"),  # child
    )
    id_type = models.CharField(max_length=3, choices=id_type_choices)

    id_number = models.CharField(max_length=18)

    tel_number = models.CharField(max_length=11)

    is_inhabitant = models.BooleanField()

    area_type_choices = (
        ("cit", "城市"),
        ("cou", "农村"),
    )
    area_type = models.CharField(max_length=3, choices=area_type_choices)

    district = models.CharField(max_length=5)

    street = models.CharField(max_length=10)

    address = models.CharField(max_length=50)  # 定为50是为了保险，防止地址过长

    departure = models.CharField(max_length=50)

    date = models.DateField(auto_now_add=True)  # 来（返）沈时间

    is_wu_han = models.BooleanField()
    is_wen_zhou = models.BooleanField()
    is_hu_bei = models.BooleanField()  # 是否途径湖北其他城市

    is_worker = models.BooleanField()
    company_name = models.CharField(max_length=30, null=True)

    is_stu = models.BooleanField()
    school_name = models.CharField(max_length=30, null=True)

    is_guest = models.BooleanField()
    hotel_name = models.CharField(max_length=30, null=True)
