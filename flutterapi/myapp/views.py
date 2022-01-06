from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import TodolistSerializer
from .models import Todolist

@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all()
    serializer = TodolistSerializer(alltodolist, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_todolist(request, TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data = {}
        serializer = TodolistSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['status']='Update Complate'
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_todolist(request, TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == "DELETE":
        delete = todo.delete()
        data = {}
        if delete:
            data['status'] = 'Delete'
            statuscode = status.HTTP_200_OK
        else:
            data['status']= 'failed'
            statuscode = status.HTTP_400_BAD_REQUEST

    return Response(data=data, status=statuscode)




data = [
    {
        "title":"คอมพิวเตอร์คืออะไร?",
        "subtitle":"คอมพิวเตอร์คืออุปกรที่ใช้สำหรับการคำนวณและทำงานอื่นๆ",
        "image_url":"https://raw.githubusercontent.com/pisit4449/BasicAPI/main/computer1.jpg",
        "detail":"คอมพิวเตอร์ (อังกฤษ: computer) หรือศัพท์บัญญัติราชบัณฑิตยสภาว่า คณิตกรณ์[2][3] เป็นเครื่องจักรแบบสั่งการได้ที่ออกแบบมาเพื่อดำเนินการกับลำดับตัวดำเนินการทางตรรกศาสตร์หรือคณิตศาสตร์ โดยอนุกรมนี้อาจเปลี่ยนแปลงได้เมื่อพร้อม ส่งผลให้คอมพิวเตอร์สามารถแก้ปัญหาได้มากมาย\n\nคอมพิวเตอร์ถูกประดิษฐ์ออกมาให้ประกอบไปด้วยความจำรูปแบบต่าง ๆ เพื่อเก็บข้อมูล อย่างน้อยหนึ่งส่วนที่มีหน้าที่ดำเนินการคำนวณเกี่ยวกับตัวดำเนินการทางตรรกศาสตร์ และตัวดำเนินการทางคณิตศาสตร์ และส่วนควบคุมที่ใช้เปลี่ยนแปลงลำดับของตัวดำเนินการโดยยึดสารสนเทศที่ถูกเก็บไว้เป็นหลัก อุปกรณ์เหล่านี้จะยอมให้นำเข้าข้อมูลจากแหล่งภายนอก และส่งผลจากการคำนวณตัวดำเนินการออกไป"
    },
    {
        "title":"มาเขียนโปรแกรมกันเถอะ",
        "subtitle":"บทความนี้จะแนนำการเริ่มต้นเขียนโปรแกรม",
        "image_url":"https://raw.githubusercontent.com/pisit4449/BasicAPI/main/computer2.jpg",
        "detail":"การเขียนโปรแกรมคอมพิวเตอร์ (อังกฤษ: Computer programming) หรือเรียกให้สั้นลงว่า การเขียนโปรแกรม (อังกฤษ: Programming) หรือ การเขียนโค้ด (Coding) เป็นขั้นตอนการเขียน ทดสอบ และดูแลซอร์สโค้ดของโปรแกรมคอมพิวเตอร์ ซึ่งซอร์สโค้ดนั้นจะเขียนด้วยภาษาโปรแกรม ขั้นตอนการเขียนโปรแกรมต้องการความรู้ในหลายด้านด้วยกัน เกี่ยวกับโปรแกรมที่ต้องการจะเขียน และขั้นตอนวิธีที่จะใช้ ซึ่งในวิศวกรรมซอฟต์แวร์นั้น \n\nการเขียนโปรแกรมถือเป็นเพียงขั้นหนึ่งในวงจรชีวิตของการพัฒนาซอฟต์แวร์การเขียนโปรแกรมจะได้มาซึ่งซอร์สโค้ดของโปรแกรมนั้นๆ โดยปกติแล้วจะอยู่ในรูปแบบของ ข้อความธรรมดา ซึ่งไม่สามารถนำไปใช้งานได้ จะต้องผ่านการคอมไพล์ตัวซอร์สโค้ดนั้นให้เป็นภาษาเครื่อง (Machine Language) เสียก่อนจึงจะได้เป็นโปรแกรมที่พร้อมใช้งาน"
    },
    {
        "title":"Flutter คืออะไร",
        "subtitle":"Tools สำหรับออกแบบ UI ใน Google",
        "image_url":"https://raw.githubusercontent.com/pisit4449/BasicAPI/main/coding.jpg",
        "detail":"เรามาเริ่มกับ Palm กันในปี 1996 ยุคที่คนเริ่มหันมาสนใจเรื่องของหน้าตาโทรศัพท์ จอเริ่มใหญ่ขึ้นเเละสามารถปากกาจิ้มที่หน้าจอได้ ซึ่งยุคนั้นต้องยกให้ Palm (PDA) เครื่องจะคล้ายๆ กับเครื่องคิดเลขขนาดใหญ่ ต้องเรียนรู้วิธีใช้ ซึ่งเจ้า palm เนี้ยใช้ C++ ในการพัฒนาเเละใช้ browser ในการ run โดยใช้ WAB(Wireless Application Browser Protocol)https://en.wikipedia.org/wiki/Palm_(PDA)#/media/File:Palm_TX.JPGต่อมาปี 2002 ทาง Nokia Prism Ericsson สามบริษัทร่วมมือกัน สร้างมือถือรุ่นฝาพับโดยใช้ภาษา Symbian พัฒนาขึ้นซึ่งตอนนั้นก็น่าจะเป็นรุ่น Nokia_7650"
    }

]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii': False})