from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse, HttpResponse

from .models import AreaInfo, PersonInfo


# Create your views here.

def index(request):
    return render(request, "permit/index.html")


def submit(request):
    """先进行审核，再跳转页面"""
    name = request.POST["name"]
    is_male = True if request.POST["sex"] == "male" else False
    id_type = request.POST["id-type"]
    id_number = request.POST["id-number"]
    tel_number = request.POST["tel-number"]
    is_inhabitant = True if request.POST["is-inhabitant"] == "yes" else False
    area_type = request.POST["area-type"]
    district = request.POST["district"]
    street = request.POST["street"]
    address = request.POST["address"]

    departure = request.POST["departure"]
    date = request.POST["date"]
    is_wu_han = True if request.POST["is-wu-han"] == "yes" else False
    is_wen_zhou = True if request.POST["is-wen-zhou"] == "yes" else False
    is_hu_bei = True if request.POST["is-hu-bei"] == "yes" else False

    is_worker = True if request.POST["is-worker"] == "yes" else False
    company_name = "" if "company-name" not in request.POST else request.POST["company-name"]
    is_stu = True if request.POST["is-stu"] == "yes" else False
    school_name = "" if "school-name" not in request.POST else request.POST["school-name"]
    is_guest = True if request.POST["is-guest"] == "yes" else False
    hotel_name = "" if "hotel_name" not in request.POST else request.POST["hotel-name"]

    person_info = PersonInfo(name=name,
                             is_male=is_male,
                             id_type=id_type,
                             id_number=id_number,
                             tel_number=tel_number,
                             is_inhabitant=is_inhabitant,
                             area_type=area_type,
                             district=district,
                             street=street,
                             address=address,
                             departure=departure,
                             date=date,
                             is_wu_han=is_wu_han,
                             is_wen_zhou=is_wen_zhou,
                             is_hu_bei=is_hu_bei,
                             is_worker=is_worker,
                             company_name=company_name,
                             is_stu=is_stu,
                             school_name=school_name,
                             is_guest=is_guest,
                             hotel_name=hotel_name,
                             )

    person_info.save()

    return redirect(reverse("permit:success", args=(person_info.id,)))


def success(request, id_number):
    """成功时候的页面"""
    person = PersonInfo.objects.get(id=id_number)

    context = {
        "name": person.name,
        "district": person.district,
        "street": person.street,
        "id_number": id_number,
    }

    return render(request, "permit/success.html", context=context)


def detail(request, id_number):
    person = PersonInfo.objects.get(id=id_number)

    context = {
        "name": person.name,
        "sex": "男" if person.is_male else "女",
        "id_type": person.id_type,
        "id_number": person.id_number,
        "tel_number": person.tel_number,
        "is_inhabitant": "是" if person.is_inhabitant else "否",
        "area_type": person.area_type,
        "district": person.district,
        "street": person.street,
        "address": person.address,
        "departure": person.departure,
        "date": person.date.isoformat(),
        "is_wu_han": "是" if person.is_wu_han else "否",
        "is_wen_zhou": "是" if person.is_wen_zhou else "否",
        "is_hu_bei": "是" if person.is_hu_bei else "否",
        "company_name": person.company_name if person.company_name else "非集中住宿务工人员",
        "school_name": person.school_name if person.school_name else "非集中住宿在校学生",
        "hotel_name": person.hotel_name if person.hotel_name else "非宾馆酒店住宿客人",
    }

    return render(request, "permit/detail.html", context=context)


def get_area_data(request):
    data = []
    search_type = request.GET.get("search")

    # 如果搜索的是区县信息
    if search_type == "district":
        models = AreaInfo.objects.filter(identifier__regex="^A0201[0-9]{2}$")

        for model in models:
            data.append(model.name)

        # 这里必须传递一个字典或者是一个 mapping，就是 xxx=xxx 的格式
        return JsonResponse({"data": data})
    # 如果搜索的是街道信息
    elif search_type == "street":
        district_name = request.GET.get("district")
        identifier = AreaInfo.objects.get(name=district_name).identifier

        models = AreaInfo.objects.filter(identifier__regex=identifier + "[0-9]{2}$")

        for model in models:
            data.append(model.name)

        return JsonResponse({"data": data})
    else:
        return JsonResponse({"value": "E0001"})


def get_site(request):
    """返回详细内容的网址"""
    id_number = request.GET["id_number"]

    return HttpResponse(request.build_absolute_uri(reverse("permit:detail", args=(id_number,))))
