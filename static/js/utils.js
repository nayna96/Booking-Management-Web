function showProjectData(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
        var _id = response["selectedProjectDetails"]["_id"];
        document.getElementById("_id").value = _id;
        document.getElementById("project_name").value = response["selectedProjectDetails"]["project_name"];
        document.getElementById("addLine1").value = response["selectedProjectDetails"]["addLine1"];
        document.getElementById("addLine2").value = response["selectedProjectDetails"]["addLine2"];
        document.getElementById("district").value = response["selectedProjectDetails"]["district"];
        document.getElementById("city").value = response["selectedProjectDetails"]["city"];
        document.getElementById("state").value = response["selectedProjectDetails"]["state"];
        document.getElementById("pin").value = response["selectedProjectDetails"]["pin"];

        approved_banks = response["selectedProjectDetails"]["approved_banks"];
        for(var i=0; i<approved_banks.length; i++){
          $("#id_fs1-" + i + "-bank_name").val(approved_banks[i]["bank_name"]);
        }

        landarea = response["selectedProjectDetails"]["landarea"];
        for(var i=0; i<landarea.length; i++){
          $("#id_fs2-" + i + "-mouza").val(landarea[i]["mouza"]);
          $("#id_fs2-" + i + "-khata_no").val(landarea[i]["khata_no"]);
          $("#id_fs2-" + i + "-plot_no").val(landarea[i]["plot_no"]);
          $("#id_fs2-" + i + "-kisam").val(landarea[i]["kisam"]);
          $("#id_fs2-" + i + "-area").val(landarea[i]["area"]);
        }

        document.getElementById("devAuth_approval_no").value = response["selectedProjectDetails"]["devAuth_approval_no"];
        document.getElementById("devAuth_approval_fromdate").value = response["selectedProjectDetails"]["devAuth_approval_fromdate"];
        document.getElementById("devAuth_approval_todate").value = response["selectedProjectDetails"]["devAuth_approval_todate"];
        document.getElementById("renewal_devAuth_approval_no").value = response["selectedProjectDetails"]["renewal_devAuth_approval_no"];
        document.getElementById("renewal_devAuth_approval_fromdate").value = response["selectedProjectDetails"]["renewal_devAuth_approval_fromdate"];
        document.getElementById("renewal_devAuth_approval_todate").value = response["selectedProjectDetails"]["renewal_devAuth_approval_todate"];
        document.getElementById("rera_certificate_no").value = response["selectedProjectDetails"]["rera_certificate_no"];
        document.getElementById("rera_certificate_fromdate").value = response["selectedProjectDetails"]["rera_certificate_fromdate"];
        document.getElementById("rera_certificate_todate").value = response["selectedProjectDetails"]["rera_certificate_todate"];
        document.getElementById("renewal_rera_certificate_no").value = response["selectedProjectDetails"]["renewal_rera_certificate_no"];
        document.getElementById("renewal_rera_certificate_fromdate").value = response["selectedProjectDetails"]["renewal_rera_certificate_fromdate"];
        document.getElementById("renewal_rera_certificate_todate").value = response["selectedProjectDetails"]["renewal_rera_certificate_todate"];

        showFiles("Master", "Project", response["files"])
      },
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";   
}

function showBlockData(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
      },
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";   
}

function showFlatData(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
      },
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";   
}

function showCustomerData(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
        var _id = response["selectedCustomerDetails"]["_id"];
        document.getElementById("_id").value = _id;
        document.getElementById("customer_salutation").value = response["selectedCustomerDetails"]["customer_salutation"];
        document.getElementById("customer_fname").value = response["selectedCustomerDetails"]["customer_fname"];
        document.getElementById("customer_mname").value = response["selectedCustomerDetails"]["customer_mname"];
        document.getElementById("customer_lname").value = response["selectedCustomerDetails"]["customer_lname"];
        document.getElementById("customer_dob").value = response["selectedCustomerDetails"]["customer_dob"];
        document.getElementById("customer_gender").value = response["selectedCustomerDetails"]["customer_gender"];

        document.getElementById("co-owner_salutation").value = response["selectedCustomerDetails"]["co-owner_salutation"];
        document.getElementById("co-owner_fname").value = response["selectedCustomerDetails"]["co-owner_fname"];
        document.getElementById("co-owner_mname").value = response["selectedCustomerDetails"]["co-owner_mname"];
        document.getElementById("co-owner_lname").value = response["selectedCustomerDetails"]["co-owner_lname"];
        document.getElementById("co-owner_dob").value = response["selectedCustomerDetails"]["co-owner_dob"];
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

        showFiles("Master", "Customer", response["files"])
      }, 
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";        
}

function showBankData(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
      },
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";   
}

function showBookingEntry(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
      },
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";   
}

function showCustomerRequest(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
      },
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";   
}

function showUserData(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
      },
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";   
}