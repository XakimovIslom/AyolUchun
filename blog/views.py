from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework.response import Response
from blog.models import Region, District, School, Student, Test
from django.db import models
from django.contrib.postgres.aggregates import ArrayAgg
from django.contrib.postgres.expressions import ArraySubquery
from django.db.models.functions import JSONObject
from django.db.models import OuterRef
from django.db.models.functions import Coalesce


class BlogListAPIView(generics.GenericAPIView):

    def get(self, request):
        # regions = Region.objects.all().annotate(
        #     student_res=models.Avg("districts__schools__students__tests__percentage")
        # )
        # # print(regions.__dict__)
        # for region in regions:
        #     print(region.student_res)

        # 2
        # districts = (
        #     District.objects.filter(region_id=OuterRef("id"))
        #     .annotate(
        #         result=Coalesce(models.Avg("schools__students__tests__percentage"), 0)
        #     )
        #     .values(json=JSONObject(title="title", result="result"))
        #     .order_by("-result", "title")[:3]
        # )
        # regions = Region.objects.all().annotate(student_res=ArraySubquery(districts))
        # print(regions.__dict__)
        # for region in regions:
        #     print(region.title)
        #     print(region.student_res)
        #     print("___________")

        # 4
        # months = {
        #     "yanvar": [],
        #     "fevral": [],
        #     "mart": [],
        #     "aprel": [],
        #     "may": [],
        #     "iyun": [],
        #     "iyul": [],
        #     "avgust": [],
        #     "sentabr": [],
        #     "oktabr": [],
        #     "noyabr": [],
        #     "dekabr": [],
        # }
        # annotates = {}
        # index = 1
        # for month in months:
        #     annotates[month] = Coalesce(
        #         models.Avg(
        #             "districts__schools__students__tests__percentage",
        #             filter=models.Q(
        #                 districts__schools__students__tests__created_at__month=index
        #             ),
        #         ),
        #         0.0,
        #         output_field=models.DecimalField(),
        #     )
        #     index += 1
        # regions = Region.objects.all().annotate(**annotates)
        # for region in regions:
        #     for month in months:
        #         months[month].append(
        #             {"title": region.title, "result": getattr(region, month)}
        #         )

        # 5
        # regions = Region.objects.all().annotate(
        #     student_res=models.Sum(
        #         models.Case(
        #             models.When(
        #                 districts__schools__students__tests__percentage__gte=80, then=1
        #             ),
        #             models.When(
        #                 districts__schools__students__tests__percentage__gte=50,
        #                 then=0.5,
        #             ),
        #             default=0,
        #             output_field=models.DecimalField(),
        #         )
        #     )
        # )
        # for region in regions:
        #     print(region.title)
        #     print(region.student_res)
        #     print("___________")
        return Response("hello")
