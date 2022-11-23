$(document).ready(function () {
  
  var hashes = window.location.href.slice(window.location.href.indexOf('?'))
    var i=hashes.indexOf(":")+1
    var j=hashes.indexOf(",")
    var pid=hashes.slice(i,j)
    // alert(pid)


  $.getJSON('/fetch_cart',function(data){
    // alert(data.data)
    var cart=JSON.parse(data.data)
    var key=Object.keys(cart)
    // alert(key)
    // alert(key.length)
    $('#shoppingcart').html(`Cart(${key.length})&nbsp;&nbsp;&nbsp;`)
    if(key.includes(pid)) 
    {
      $('.addtocart').hide()
      $('#qtycomponent').show()
      $('#qty').html(cart[pid]['qty'])
    }
    else
    {
      $('#qtycomponent').hide()
    }
  
  })


  $('#qtycomponent').hide()
  $("#user-menu-button").click(function () {
    $("#dropdown").toggle();
  });

  // Category Fetch

  $.getJSON("http://localhost:8000/fetch_all_user_category", function (data) {
    var htm = "";
    data.data.map((item) => {
      htm += `
        <div style="margin:5px;
                    
                    width:auto;
                    background: #fff; 
                    height: 30px; 
                    border-radius: 50px; 
                    display: flex;
                    flex-direction: row;
                    font-family: -webkit-body;
                    font-size: small;">`;
        htm += `
           <div style="display:flex; flex-direction: column;">          
           <div style="padding: 5px;">   
              <a href="" style="color:black">           
              ${item.categoryname}
              </a>              
           </div>              
           </div>`;
        htm += `</div>`;
    });
    // console.log(htm)
    $("#catid").html(htm);
  });


  // Product Fetch

  $.getJSON('http://localhost:8000/fetch_all_products', function (data) {
      
    var htm = ''
          
    data.data.map((item) => {
      var price
      var offerprice
      var save
      if (item.productofferprice > 0) {
        price = item.productprice
        offerprice = item.productofferprice
        save = (item.productprice - item.productofferprice)/100
      }
      else {
        price = item.productprice
        offerprice = "<div></div>"
        save = "<div></div>"
      }
      
      var data = JSON.stringify(item)
      // alert(data)
      // alert(data.length)
      htm += `
     
         <div 
             style="width:260px;
                   padding:15px;
                   height:auto;
                   background-color:#FFF;
                   border:2px solid #FFF;
                   border-radius:10px;
                   display:flex;
                   flex-direction:column; 
                   align-items:center;
                   margin:20px 0px 20px 40px;
                   box-shadow: 0 6px 12px -4px rgb(11 18 25 / 10%);
                   elevation: below;">
                <div> <a href='http://localhost:8000/buy_product?product=${data}'style="text-decoration: none">
                   <img  src="http://localhost:8000/static/${item.producticon}" 
                         width="120" 
                         height="140" 
                         alt="product-img"></a><hr width='100%'>
                </div>

           <div style="font-weight:600;
                       width:200px;
                       text-align:left;
                       font-size:17px;">
              ${item.productname}
           </div>

           <div style="text-align:left;
                       font-size:12px;
                       width:200px;">
              <i>Mkt:${item.bname}</i>
          </div>

          <div style="text-align:left;
                      color:red;font-weight:600;
                      width:200px;">
            &#8377;<strike>${price}</strike>
          </div>

          <div style="text-align:left;
                      font-weight:600;
                      width:200px;">
            &#8377;${offerprice}
          </div>

          <div style="text-align:left;
                      color:green;
                      font-weight:600;
                      width:200px;">
            UPTO ${save}% OFF
          </div>

           
      </div>`
    })
    $('#productlist').html(htm)
  })



  // Subcategory Fetch

  $.getJSON(
    "http://localhost:8000/fetch_all_subcategory_json",
    function (data) {
      var htm = "";
      data.data.map((item) => {
        htm += `
        <div style="margin:5px;                    
                    width:300px;
                    background: #fff; 
                    height: auto; 
                    border-radius: 10px; 
                    display: flex;
                    flex-direction: row">`;
        htm += `
        <div style="padding: 5px">
           <img src='/static/${item.subcategoryicon}' width="40">
        </div>`;
        htm += `
        <div style="display:flex; 
                    flex-direction: column;">

            <div style="font-weight: bold; padding: 5px">
            ${item.subcategoryname}
            </div>
            <div style="font-size: x-small; margin-left: 5px">
            Save upto 15%       
            </div>        
        </div>`;
        htm += `</div>`;
      });
      $("#subcategorylist").html(htm);
    }
  );

  
  // Plus minus qty
  $('.plus').click(function(){
    // alert(1)
    var v=$('#qtyac').html()
    if(v<=4)
       v++
    $('#qtyac').html(v)
    cartContainer($(this).attr('product'),$('#qtyac').html())

  })

  $('.minus').click(function(){
    var v=$('#qtyac').html()
    if(v>0)
    v--
    if(v==0) {
        $('.addtocart').show()
        $('#qtycomponent').hide()
        alert($(this).attr('productid'))
        removeCartContainer($(this).attr('productid'))  
      }
    else
    {
    cartContainer($(this).attr('product'),$('#qtyac').html())
    $('#qtyac').html(v)
    }
  })

  $('.addtocart').click(function(){
    $('.addtocart').hide()
    $('#qtycomponent').show()
    $('#qtyac').html(1)
    cartContainer($(this).attr('product'),$('#qtyac').html())
  })


function cartContainer(product,qtyac){
  $.getJSON('/add_to_cart',{'product':product,'qtyac':qtyac},function(data){
    // alert(data.data)
    var cart=JSON.parse(data.data)
    var key=Object.keys(cart)
    // alert(key)
    // alert(key.length)
    $('#shoppingcart').html(`Cart(${key.length})&nbsp;&nbsp;&nbsp;`)
  })
}

function removeCartContainer(productid) {
  $.getJSON('/remove_from_cart', {'productid':productid}, function (data) {
      alert('removed')
      var cart=JSON.parse(data.data)
      var key=Object.keys(cart)
        $('#shoppingcart').html(`Cart(${key.length})&nbsp;&nbsp;&nbsp;`)
 
         })
 }

});
