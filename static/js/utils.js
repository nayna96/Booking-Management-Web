function showCustomers_Data(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
        var _id = response["selectedCustomerDetails"]["_id"];
        $("#_id").val(_id);

        document.getElementById("customer_salutation").value = response["selectedCustomerDetails"]["customer_salutation"];
        document.getElementById("customer_fname").value = response["selectedCustomerDetails"]["customer_fname"];
        document.getElementById("customer_mname").value = response["selectedCustomerDetails"]["customer_mname"];
        document.getElementById("customer_lname").value = response["selectedCustomerDetails"]["customer_lname"];
        document.getElementById('customer_dob').value = response["selectedCustomerDetails"]["customer_dob"];
        document.getElementById("customer_gender").value = response["selectedCustomerDetails"]["customer_gender"];

        document.getElementById("co-owner_salutation").value = response["selectedCustomerDetails"]["co-owner_salutation"];
        document.getElementById("co-owner_fname").value = response["selectedCustomerDetails"]["co-owner_fname"];
        document.getElementById("co-owner_mname").value = response["selectedCustomerDetails"]["co-owner_mname"];
        document.getElementById("co-owner_lname").value = response["selectedCustomerDetails"]["co-owner_lname"];
        document.getElementById('co-owner_dob').value = response["selectedCustomerDetails"]["co-owner_dob"];
        document.getElementById("co-owner_gender").value = response["selectedCustomerDetails"]["co-owner_gender"];

        document.getElementById("email").value = response["selectedCustomerDetails"]["email"];
        document.getElementById("mobile_no").value = response["selectedCustomerDetails"]["mobile_no"];
        document.getElementById("whatsapp_no").value = response["selectedCustomerDetails"]["whatsapp_no"];
  
        document.getElementById("father_husband's_salutation").value = response["selectedCustomerDetails"]["father_husband's_salutation"];
        document.getElementById("father_husband's_name").value = response["selectedCustomerDetails"]["father_husband's_name"];
        document.getElementById("relation").value = response["selectedCustomerDetails"]["relation"];

        document.getElementById("copy_present").value = response["selectedCustomerDetails"]["copy_present"];

        document.getElementById("pr_addLine1").value = response["selectedCustomerDetails"]["pr_addLine1"];
        document.getElementById("pr_addLine2").value = response["selectedCustomerDetails"]["pr_addLine2"];
        document.getElementById("pr_district").value = response["selectedCustomerDetails"]["pr_district"];
        document.getElementById("pr_city").value = response["selectedCustomerDetails"]["pr_city"];
        document.getElementById("pr_state").value = response["selectedCustomerDetails"]["pr_state"];
        document.getElementById("pr_pincode").value = response["selectedCustomerDetails"]["pr_pincode"];

        document.getElementById("pe_addLine1").value = response["selectedCustomerDetails"]["pe_addLine1"];
        document.getElementById("pe_addLine2").value = response["selectedCustomerDetails"]["pe_addLine2"];
        document.getElementById("pe_district").value = response["selectedCustomerDetails"]["pe_district"];
        document.getElementById("pe_city").value = response["selectedCustomerDetails"]["pe_city"];
        document.getElementById("pe_state").value = response["selectedCustomerDetails"]["pe_state"];
        document.getElementById("pe_pincode").value = response["selectedCustomerDetails"]["pe_pincode"];

        document.getElementById("copy_from").value = response["selectedCustomerDetails"]["copy_from"];
        document.getElementById("contact_p_salutation").value = response["selectedCustomerDetails"]["contact_p_salutation"];
        document.getElementById("contact_p_name").value = response["selectedCustomerDetails"]["contact_p_name"];
        document.getElementById("contact_p_phone_no").value = response["selectedCustomerDetails"]["contact_p_phone_no"];

        document.getElementById("broker's_salutation").value = response["selectedCustomerDetails"]["broker's_salutation"];
        document.getElementById("broker's_name").value = response["selectedCustomerDetails"]["broker's_name"];

        document.getElementById("occupation").value = response["selectedCustomerDetails"]["occupation"];
        document.getElementById("caste").value = response["selectedCustomerDetails"]["caste"];

        document.getElementById("username").value = response["selectedCustomerDetails"]["username"];
        document.getElementById("password").value = response["selectedCustomerDetails"]["password"];

        document.getElementById("bank_name").value = response["selectedCustomerDetails"]["bank_name"];
        document.getElementById("branch_name").value = response["selectedCustomerDetails"]["branch_name"];
        document.getElementById("account_type").value = response["selectedCustomerDetails"]["account_type"];
        document.getElementById("account_no").value = response["selectedCustomerDetails"]["account_no"];

        document.getElementById("aadhar_no").value = response["selectedCustomerDetails"]["aadhar_no"];
        document.getElementById("pan_no").value = response["selectedCustomerDetails"]["pan_no"];
        document.getElementById("voter_id").value = response["selectedCustomerDetails"]["voter_id"];
        document.getElementById("gst_no").value = response["selectedCustomerDetails"]["gst_no"];

        showFiles(response["files"])
      }, 
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";        
}

function showFiles(files_dt) {      
  files_dt.forEach ((file) =>
  {
    var docName = file.metadata["doc_name"];
    var _path = file.filename;
      switch (docName)
      {
          case "passport_photo":
            
            break;
          case "aadhar_card":
            UpdateDiv("aadharCard", _path)
            break;
          case "pan_card":
            UpdateDiv("panCard", _path)  
            break;
          case "voter_id_card":
            UpdateDiv("voterIDCard", _path)    
            break;
          case "gst_doc":
            UpdateDiv("gstDoc", _path)    
            break;
          case "other_docs":
            UpdateDiv("otherDocs", _path)                  
              break;
          default:
              break;
      }
  });
}

function UpdateDiv(divID, file){
  var myList = document.getElementById(divID).getElementsByTagName('ul')[0];
  var myNewListItem = document.createElement('li');
  myNewListItem.innerHTML = "<a href='#' onclick=viewFile('/view/Master/" + encodeURIComponent(file) + "')>" + file + "</a>"
  myList.appendChild(myNewListItem);
}

function viewFile(_url){
  $.ajax({      
    url: _url
  });
}

function resetDiv(){
  var div = document.getElementById("aadharCard");
  div.innerHTML = "<ul></ul>";

  var div = document.getElementById("panCard");
  div.innerHTML = "<ul></ul>";

  var div = document.getElementById("voterIDCard");
  div.innerHTML = "<ul></ul>";

  var div = document.getElementById("gstDoc");
  div.innerHTML = "<ul></ul>";

  var div = document.getElementById("otherDocs");
  div.innerHTML = "<ul></ul>";
}