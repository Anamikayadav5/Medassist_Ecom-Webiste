$(document).ready(function(){

// Fetch All Category
     $.getJSON('http://localhost:8000/fetchallcategoryjson',function(data){
     var records=data.data
//     alert(JSON.stringify(data))
     records.map((item)=>{
        $('#categoryid').append($("<option>").text(item.categoryname).val(item.categoryid))
     })
     $('select').formSelect();
     })

//  Fetch all SubCategory
   $('#categoryid').change(function(){
         $('#subcategoryid').empty()
          $.getJSON("http://localhost:8000/fetchallsubcategoryjson",{categoryid:$('#categoryid').val()},function (data){
//       alert(JSON.stringify(data))
        $('#subcategoryid').append($("<option>").text('Select SubCategory'))
        var records=data.data

        records.map ((item)=>{
            $('#subcategoryid').append($("<option>").text(item.subcategoryname).val(item.subcategoryid))
        })
        $('select').formSelect();
        })

   })

//Fetch All Brand

     $('#subcategoryid').change(function(){
            $('#brandid').empty()
            $.getJSON("http://localhost:8000/fetchallbrandjson",{subcategoryid:$('#subcategoryid').val()},function (data){
               $('#brandid').append($("<option>").text('Select Brand'))
               var records=data.data

               records.map((item)=>{
                   $('#brandid').append($("<option>").text(item.brandname).val(item.brandid))
               })
               $('select').formSelect();
            })
     })
})