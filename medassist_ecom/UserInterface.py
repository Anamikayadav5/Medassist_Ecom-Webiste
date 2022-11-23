from django.shortcuts import render
from . import Pool
from django.http import JsonResponse
import json
from urllib.parse import unquote

def AddToCart(request):
    try:
     product = request.GET['product']
     qtyac=request.GET['qtyac']
     product=product.replace("'","\"")
     product=json.loads(product)
     product['qtyac']=qtyac
     print('UPDATED PRODUCTS:',product)
     #create cart container using Session
     try:
       CART_CONTAINER=request.session['CART_CONTAINER']
       CART_CONTAINER[str(product['productid'])]=product
       request.session['CART_CONTAINER']=CART_CONTAINER

     except:
       CART_CONTAINER={}
       CART_CONTAINER[str(product['productid'])]=product
       request.session['CART_CONTAINER']=CART_CONTAINER

     print("CART_CONTAINER:",CART_CONTAINER)
     CART_CONTAINER = str(CART_CONTAINER).replace("'", "\"")

     return JsonResponse({'data': CART_CONTAINER}, safe=False)
    except Exception as err:
        print("ERRORRRRR:",err)
        return JsonResponse({'data': []}, safe=False)

def FetchCart(request):
    try:
     try:
       CART_CONTAINER=request.session['CART_CONTAINER']

     except:
       CART_CONTAINER={}

     print("CART_CONTAINER:",CART_CONTAINER)
     CART_CONTAINER = str(CART_CONTAINER).replace("'", "\"")

     return JsonResponse({'data': CART_CONTAINER}, safe=False)
    except Exception as err:
        print("ERRORRRRR:",err)
        return JsonResponse({'data': []}, safe=False)    

def RemoveFromCart(request):
    try:
       productid = request.GET['productid']

       CART_CONTAINER=request.session['CART_CONTAINER']
       del CART_CONTAINER[productid]
       request.session['CART_CONTAINER']=CART_CONTAINER
       print("REMOVE CART_CONTAINER:",CART_CONTAINER)
       CART_CONTAINER = str(CART_CONTAINER).replace("'", "\"")
       return JsonResponse({'data': CART_CONTAINER}, safe=False)
    except Exception as err:
        print("ERRORRRRR:",err)
        return JsonResponse({'data': []}, safe=False)


def Index(request):
    return render(request,"index.html")
  
def Buy_Product(request):
    product=unquote(request.GET['product'])
    # print(product)
    product=json.loads(product)
    # print("zzzzzzzzzzzzz",product)
    return render(request,"Buy_Product.html",{'product':product})
    
def Fetch_All_Products(request):
    try:
        db, cmd = Pool.ConnectionPooling()
        query = "select p.*,(select c.categoryname from categories c where c.categoryid=p.categoryid) as cname,(select s.subcategoryname from subcategories s where p.subcategoryid=s.subcategoryid) as scname,(select b.brandname from brands b where p.brandid=b.brandid) as bname from products p"
        cmd.execute(query)
        products = cmd.fetchall()
        # print('RECORDS2:', products)
        db.close()

        return JsonResponse({'data': products}, safe=False)

    except Exception as e:
        print("err",e)

        return JsonResponse({'data': []}, safe=False)

def Fetch_All_Category_JSON(request):
    try:
      DB, CMD = Pool.ConnectionPooling()
      Q = "select * from categories"
      CMD.execute(Q)
      records = CMD.fetchall()
      # print('RECORDS1:', records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)

def Fetch_All_SubCategory_JSON(request):
    try:
      DB, CMD = Pool.ConnectionPooling()
      Q = "select * from subcategories"
      CMD.execute(Q)
      records = CMD.fetchall()
      # print('RECORDS:', records)
      DB.close()
      return JsonResponse({'data': records}, safe=False)
    except Exception as e:
      print('Error:', e)
      return JsonResponse({'data': []}, safe=False)
