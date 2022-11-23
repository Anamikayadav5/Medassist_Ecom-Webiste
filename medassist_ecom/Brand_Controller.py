from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def Brand_Interface(request):
    try:
        admin = request.session['ADMIN']
        return render(request, 'BrandInterface.html')
    except:
        return render(request, 'LoginPage.html')

@xframe_options_exempt
def Submit_Brand(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid=request.POST['categoryid']
        subcategoryid=request.POST['subcategoryid']
        brandname=request.POST['brandname']
        contactperson=request.POST['contactperson']
        mobile=request.POST['mobile']
        status=request.POST['status']
        brandicon=request.FILES['brandicon']

        Q="insert into brands(categoryid,subcategoryid,brandname,contactperson,mobile,status,brandicon) values({0},{1},'{2}','{3}','{4}','{5}','{6}')".format(categoryid,subcategoryid,brandname,contactperson,mobile,status,brandicon.name)
        F=open("C:/Users/Public/django/medassist_ecom/assets"+brandicon.name,'wb')
        for chunk in brandicon.chunks():
            F.write(chunk)
        F.close()

        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request,'BrandInterface.html',{'message':'Record Submitted Succesfully'})
    except Exception as e:
        print("Error:",e)
        return render(request,'BrandInterface.html',{'message':'Failed'})


@xframe_options_exempt
def Fetch_All_SubCategory_JSON(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid=request.GET['categoryid']
        Q="select * from subcategories where categoryid={0}".format(categoryid)
        print(Q)
        CMD.execute(Q)
        records=CMD.fetchall()
        print(records)
        DB.close()
        return JsonResponse({'data':records},safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({'data':None},safe=False)
@xframe_options_exempt
def Display_All_Brand(request):
    try:
        admin = request.session['ADMIN']
    except:
        return render(request, 'LoginPage.html')
    try:
        DB, CMD = Pool.ConnectionPooling()
        Q="select B.*,(select C.categoryname from categories C where C.categoryid=B.categoryid) as cname,(select S.subcategoryname from subcategories S where B.subcategoryid=S.subcategoryid) as scname from brands B"
        CMD.execute(Q)
        records=CMD.fetchall()
        print("RECORDS:",records)
        DB.close()
        return render(request,'DisplayAllBrand.html',{'records':records})
    except Exception as e:
        print("Error:",e)
        return render(request,'DisplayAllBrand.html',{'records':None})
@xframe_options_exempt
def Edit_Brand(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid=request.GET['categoryid']
        subcategoryid=request.GET['subcategoryid']
        brandid=request.GET['brandid']
        brandname=request.GET['brandname']
        contactperson=request.GET['contactperson']
        mobile=request.GET['mobile']
        status=request.GET['status']
        Q="update brands set categoryid={0},subcategoryid={1},brandname='{2}',contactperson='{3}',mobile='{4}',status='{5}' where brandid={6}".format(categoryid,subcategoryid,brandname,contactperson,mobile,status,brandid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result':True},safe=False)
    except Exception as e:
        print("Error:",e)
        return JsonResponse({'result':False},safe=False)

@xframe_options_exempt
def Delete_Brand(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        brandid=request.GET['brandid']
        Q="delete from brands where brandid={0}".format(brandid)
        print(Q)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)

    except Exception as e:
        print("Error:", e)
        return JsonResponse({'result': False}, safe=False)
@xframe_options_exempt
def Edit_BrandIcon(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        brandid = request.POST['brandid']
        brandicon = request.FILES['brandicon']
        Q = "update brands set brandicon='{0}' where  brandid={1}".format(brandicon.name,brandid)
        print(Q)
        F = open("C:/Users/Public/django/medassist_ecom/assets" + brandicon.name, 'wb')
        for chunk in brandicon.chunks():
          F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return JsonResponse({'result': True}, safe=False)
    except Exception as e:
        print("Error:", e)
        return JsonResponse({'result': False}, safe=False)