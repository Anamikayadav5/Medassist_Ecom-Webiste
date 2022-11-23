"""medassist_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import Category_Controller
from . import SubCategory_Controller
from . import Brand_Controller
from . import Product_Controller
# from . import Dashboard_Controller
from . import Admin_Controller
from . import UserInterface



urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoryinterface/', Category_Controller.Category_Interface),
    path('submitcategory', Category_Controller.Submit_Category),
    path('displayallcategories/', Category_Controller.Display_All_Category),
    path('editcategory/', Category_Controller.Edit_Category),
    path('deletecategory/', Category_Controller.Delete_Category),
    path('editcategoryicon', Category_Controller.Edit_CategoryIcon),
    path('fetchallcategoryjson', Category_Controller.Fetch_All_Category_JSON),

    path('subcategoryinterface/', SubCategory_Controller.SubCategory_Interface),
    path('submitsubcategory', SubCategory_Controller.Submit_SubCategory),
    path('displayallsubcategories/', SubCategory_Controller.Display_All_SubCategory),
    path('editsubcategory/', SubCategory_Controller.Edit_SubCategory),
    path('deletesubcategory/', SubCategory_Controller.Delete_SubCategory),
    path('editsubcategoryicon', SubCategory_Controller.Edit_SubCategoryIcon),

    path('brandinterface/', Brand_Controller.Brand_Interface),
    path('submitbrand', Brand_Controller.Submit_Brand),
    path('fetchallsubcategoryjson/', Brand_Controller.Fetch_All_SubCategory_JSON),
    path('displayallbrands/', Brand_Controller.Display_All_Brand),
    path('editbrand/', Brand_Controller.Edit_Brand),
    path('deletebrand/', Brand_Controller.Delete_Brand),
    path('editbrandicon', Brand_Controller.Edit_BrandIcon),

    path('productinterface/', Product_Controller.Product_Interface),
    path('submitproduct', Product_Controller.Submit_Brand),
    path('fetchallbrandjson/', Product_Controller.fetchallbrandjson),
    path('displayproducts/', Product_Controller.Display_Products),
    path('editproduct/', Product_Controller.Edit_Products),
    path('deleteproduct/', Product_Controller.Delete_Products),
    path('editproductimage', Product_Controller.Edit_Product_Image),

    # path('displaydashboard/', Dashboard_Controller.Dashboard_Display),

    path('adminlogin/', Admin_Controller.Admin_Login),
    path('adminlogout/', Admin_Controller.Admin_Logout),
    path('checkadminlogin', Admin_Controller.Check_Admin_Login),

    path('home/',UserInterface.Index),
    path('fetch_all_user_category/',UserInterface.Fetch_All_Category_JSON),
    
    path('fetch_all_products/',UserInterface.Fetch_All_Products),
    path('fetch_all_subcategory_json/',UserInterface.Fetch_All_SubCategory_JSON),
    path('buy_product/',UserInterface.Buy_Product),
    
    path('add_to_cart/',UserInterface.AddToCart),
    path('fetch_cart/',UserInterface.FetchCart),
    path('remove_from_cart/',UserInterface.RemoveFromCart),
    
    
    

]
