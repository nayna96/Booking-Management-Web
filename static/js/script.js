function AccFunc(id) {
  var x = document.getElementById(id);
  if(x.classList.contains("w3-show")){
    x.classList.remove("w3-show");
    x.classList.add("w3-hide");
  } else if(x.classList.contains("w3-hide")){
    x.classList.remove("w3-hide");
    x.classList.add("w3-show");
  }
}

function showImage(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
          $('#pic')
              .attr('src', e.target.result)
              .width(150)
              .height(200);
      };

      reader.readAsDataURL(input.files[0]);
  }
}
  
function show_modal(){
  resetFileDiv();
  resetFormSet();
  document.getElementById("form").reset();

  var modal = document.getElementById("myModal");
  var span = document.getElementsByClassName("_close")[0];
  modal.style.display = "block";
  span.onclick = function() {
    modal.style.display = "none";
  }
  /*window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }*/
  document.getElementById("btn").value = "Save";
  document.getElementById("btn").name = "Save";    
} 

function getMaxDate(){
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth() + 1; //January is 0!
  var yyyy = today.getFullYear();

  if (dd < 10) {
    dd = '0' + dd;
  }

  if (mm < 10) {
    mm = '0' + mm;
  } 
      
  today = yyyy + '-' + mm + '-' + dd;
  
  return today
}

function formatDate(dateString){
  var dateParts = dateString.split("-");
  if(dateParts.length == 1){
    dateParts = dateString.split("/");
  }

  if(dateParts[2].length == 4){
    var dateObj = new Date(+dateParts[2], dateParts[1] - 1, +dateParts[0]); 
  } else{
    var dateObj = new Date(+dateParts[0], dateParts[1] - 1, +dateParts[2]); 
  }
  
  var dd = String(dateObj.getDate()).padStart(2, '0');
  var mm = String(dateObj.getMonth() + 1).padStart(2, '0'); //January is 0!
  var yyyy = dateObj.getFullYear();

  date = yyyy + '-' + mm + '-' + dd;
  return date;
}

function maxdateValidation(e){
  today = getMaxDate();
  if(e.target.value > today){
      e.target.value = "";
      alert("Date is greater than max date");
  } 
}

//Move to next tab on Enter
document.addEventListener('keydown', function (event) {
  if (event.key === "Enter" && event.target.nodeName === 'INPUT') {
    var form = event.target.form;
    var index = Array.prototype.indexOf.call(form, event.target);
    form.elements[index + 1].focus();
    event.preventDefault();
  }
});

function ifExists(db_name, collection_name, dt){
  dt = JSON.stringify(dt)
  return $.ajax({      
    url: "/ifexists/" + db_name + "/" + collection_name + "/" + dt,
    async: false,
    success: function(response){
      
    }, 
    error: function(error) {
      console.log(error)
    }
  });
}

function requiredValidation(){
  var requiredElements = document.getElementById("form").querySelectorAll("[required]");

  var s = "";
  for (var i = 0; i < requiredElements.length; i++) {
    var e = requiredElements[i];

    checked = false
    if(e.type == "radio"){
      el_name = e.name
      els = $("input[name=" + el_name + "]")
      for(var j = 0; j < els.length; j++){
        if(els[j].checked == true){
          checked = true;
          break;
        }
      }
      
      if(checked == false){
        s += "Please select either one of " +  el_name + "\n";
      }
    }

    s += e.value.length? "" : e.id + ": Not Filled" + "\n";
  }

  if(s.length > 0){
    alert(s);
    return false;
  }

  return true;
}

function AddOrdinal(num)
{
    if (num <= 0) return num;
    switch (num % 100)
    {
        case 11:
        case 12:
        case 13:
            return num + "TH";
    }
    switch (num % 10)
    {
        case 1:
            return num + "ST";
        case 2:
            return num + "ND";
        case 3:
            return num + "RD";
        default:
            return num + "TH";
    }
}

function showFlats(){
  var flats_url = $("#form").attr("data-flats-url");
  var project_name = $("#project_name").val();
  var block_name = $("#block_name").val();
  var floor_no = $("#floor_no").val();
  var share_type = ''

  var els = document.querySelectorAll("input[name='landowner_company_share']");
  for (var i = 0; i < els.length; i++) {
    if (els[i].checked) {
      share_type = els[i].value;
      break;
    }
  }

  $.ajax({
    url: flats_url,
    data: {
      'project_name': project_name,
      'block_name': block_name,
      'floor_no': floor_no,
      'share_type': share_type
    },
    success: function(result){
      var options = result["flats"];
      $('#flat_no').empty();
      $('#flat_no').append($('<option value="" selected disabled>-- Select --</option>'));
      $.each(options, function(i, p) {
        $('#flat_no').append($('<option></option>').val(p).html(p));
      })
    }
  });
}

$(document).ready(function() {
  $("#fancyTable").fancyTable({
    sortColumn:0,
    pagination: true,
    perPage:10,
    globalSearch:true
  });

  //ALLSTRING
  $('body').on('input', '.allstring', function() {
    this.value = this.value.toUpperCase();
    this.value = this.value.replace(/[^a-zA-Z .]/g, '').replace(/(\..*)\./g, '$1');
  });

  //ALLCAPS STRING
  $('body').on('input', '.allcaps', function() {
    this.value = this.value.toUpperCase();
  });
  
  //ALLNUMS 
  $('body').on('input', '.allnums', function() {
    this.value = this.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');
  });

  $("#project_name").change(function (e) {
    var block_url = $("#form").attr("data-blocks-url");
    var project_name = $("#project_name").val();

    $.ajax({
      url: block_url,
      data: {
        'project_name': project_name
      },
      success: function(result){
          var options = result["blocks"];
          $('#block_name').empty();
          $('#block_name').append($('<option value="" selected disabled>-- Select --</option>'));
          $.each(options, function(i, p) {
            $('#block_name').append($('<option></option>').val(p).html(p));
          })
      }
    });
  })

  $("#block_name").change(function (e) {
    var floor_url = $("#form").attr("data-floors-url");
    var project_name = $("#project_name").val();
    var block_name = $("#block_name").val();

    $.ajax({
      url: floor_url,
      data: {
        'project_name': project_name,
        'block_name': block_name
      },
      success: function(result){
          var options = result["floors"];
          $('#floor_no').empty();
          $('#floor_no').append($('<option value="" selected disabled>-- Select --</option>'));
          $.each(options, function(i, p) {
            $('#floor_no').append($('<option></option>').val(p).html(p));
          })
      }
    });
  })

  $("#floor_no").change(function (e) {
    showFlats();
  })

  $("#flat_no").change(function () {
    var flat_details_url = $("#form").attr("data-flat_details-url");
    var project_name = $("#project_name").val();
    var block_name = $("#block_name").val();
    var floor_no = $("#floor_no").val();
    var flat_no = $("#flat_no").val();

    $.ajax({
      url: flat_details_url,
      data: {
        'project_name': project_name,
        'block_name': block_name,
        'floor_no': floor_no,
        'flat_no': flat_no
      },
      success: function(result){
        if ('flatDetails' in result){
          $("#flat_type").val(result["flatDetails"]["flat_type"]);
          $("#carpet_area").val(result["flatDetails"]["carpet_area"]);
          $("#builtup_area").val(result["flatDetails"]["builtup_area"]);
          $("#superbuiltup_area").val(result["flatDetails"]["superbuiltup_area"]);
          $("#parking_no").val(result["flatDetails"]["parking_no"]);
          $("#parking_area").val(result["flatDetails"]["parking_area"]);
          $("#sellable_area").val(result["flatDetails"]["superbuiltup_area"]);
        }
      }
    });
  })

  $("#customer_name").change(function () {
    var customer_details_url = $("#form").attr("data-customer_details-url");
    var customer_name = $("#customer_name").val();

    $.ajax({
      url: customer_details_url,
      data: {
        'customer_name': customer_name
      },
      success: function(result){
        address = 
        result["customerDetails"]["pr_addLine1"] + 
        result["customerDetails"]["pr_addLine2"] +
        result["customerDetails"]["pr_city"] + 
        result["customerDetails"]["pr_state"] + 
        result["customerDetails"]["pr_pincode"];

        $("#address").val(address);
        $("#mobile_no").val(result["customerDetails"]["mobile_no"]);
        $("#whatsapp_no").val(result["customerDetails"]["whatsapp_no"]);
      }
    });
  })

});
