from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt

def Product_Interface(request):
    try:
        admin = request.session['ADMIN']
        return render(request, 'ProductInterface.html')
    except:
        return render(request, 'LoginPage.html')

@xframe_options_exempt
def Submit_Brand(request):
    try:
        DB, CMD = Pool.ConnectionPooling()
        categoryid = request.POST['categoryid']
        subcategoryid = request.POST['subcategoryid']
        brandid = request.POST['brandid']
        productname = request.POST['productname']
        productprice = request.POST['productprice']
        productofferprice = request.POST['productofferprice']
        quantity = request.POST['quantity']
        packingtype=request.POST['packingtype']
        productstatus = request.POST['productstatus']
        productsalestatus = request.POST['productsalestatus']

        producticon = request.FILES['producticon']
        rating = request.POST['rating']

        Q = "insert into products(categoryid,subcategoryid,brandid,productname,productprice,productofferprice,quantity,packingtype,productstatus,productsalestatus,producticon,rating) values({0},{1},{2},'{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(
            categoryid, subcategoryid, brandid, productname, productprice, productofferprice, quantity,packingtype, productstatus,
            productsalestatus, producticon.name, rating)
        F=open("C:/Users/Public/django/medassist_ecom/assets" + producticon.name, 'wb')
        for chunk in producticon.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'ProductInterface.html', {'message': 'Record Submitted Succesfully'})

    except Exception as e:
           print("Error:", e)
    return render(request, 'ProductInterface.html', {'message': 'Failed'})


@xframe_options_exempt
def Display_Products(request):
    try:
        admin = request.session['ADMIN']
    except Exception as e:
        return render(request, "LoginPage.html")
    try:
        db, cmd = Pool.ConnectionPooling()
        q = 'select P.*,(select categoryname from categories C where C.categoryid=P.categoryid) as catname,(select subcategoryname from subcategories S where S.subcategoryid=P.subcategoryid) as subcatname,(select brandname from brands B where B.brandid=P.brandid) as brandname from products P'

        cmd.execute(q)
        record = cmd.fetchall()
        db.close()
        return render(request, "DisplayAllProduct.html", {'records': record})
    except Exception as e:
        print('ERROR:', e)
        return render(request, "DisplayAllProduct.html", {'records': record})


@xframe_options_exempt
def Edit_Products(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        productid = request.GET['productid']
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        brandid = request.GET['brandid']
        productname = request.GET['productname']
        price = request.GET['productprice']
        offerprice = request.GET['productofferprice']
        packingtype = request.GET['packingtype']
        quantity = request.GET['quantity']
        status = request.GET['productstatus']
        rating = request.GET['rating']
        salestatus = request.GET['productsalestatus']

        q = "update products set categoryid={0},subcategoryid={1},brandid={2},productname='{3}',productprice='{4}',productofferprice='{5}',packingtype='{6}',quantity='{7}',productstatus='{8}',rating='{9}',productsalestatus='{10}' where productid={11}".format(
            categoryid, subcategoryid, brandid, productname, price, offerprice, packingtype, quantity, status, rating,
            salestatus, productid)
        cmd.execute(q)
        db.commit()
        print(q)
        db.close()
        return JsonResponse({'result': "True"}, safe=False)
    except Exception as e:
        print('ERROR:', e)
        return JsonResponse({'result': "False"}, safe=False)

@xframe_options_exempt
def Delete_Products(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        productid = request.GET['productid']
        q = "delete from products where productid={0}".format(productid)
        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse({'result': "True"}, safe=False)
    except Exception as e:
        print('ERROR:', e)
        return JsonResponse({'result': 'False'}, safe=False)


@xframe_options_exempt
def Edit_Product_Image(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        productid = request.POST['productid']
        productimage = request.FILES['producticon']
        q = "update products set producticon='{0}' where productid={1}".format(productimage.name, productid)
        F = open("C:/Users/Public/django/medassist_ecom/assets" + productimage.name, "wb")
        for chunk in productimage.chunks():
            F.write(chunk)
        F.close()
        cmd.execute(q)
        print(q)
        db.commit()
        db.close()
        return JsonResponse({'result': True}, safe=False)
    except Exception as e:
        print('ERROR:', e)
        return JsonResponse({'result': False}, safe=False)
@xframe_options_exempt
def fetchallbrandjson(request):
    try:
        db,cmd=Pool.ConnectionPooling()
        subcategoryid=request.GET['subcategoryid']
        q="select * from brands where subcategoryid={0}".format(subcategoryid)
        cmd.execute(q)
        print(q)
        records=cmd.fetchall()
        print(records)
        db.close()
        return JsonResponse({'data':records},safe=False)
    except Exception as e:
        print("ERROR:",e)
        return JsonResponse({'data':None},safe=False)