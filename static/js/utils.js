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

        //APPROVED BANKS
        approved_banks = response["selectedProjectDetails"]["approved_banks"];
        var length = document.getElementsByClassName("fs1").length;
        $("#fs1-fields").val(length);

        for(var i=0; i< approved_banks.length -1; i++){
          if(length != approved_banks.length){          
            addRow(undefined, "fs1");
          }
        }

        for(var i=0; i<approved_banks.length; i++){
          $("#fs1-" + i + "-bank_name").val(approved_banks[i]["bank_name"]);
        }
        //End APPROVED BANKS

        var project_status = response["selectedProjectDetails"]["project_status"];
        if(project_status == "Company Project"){
          $("#company_project").prop("checked", true);
          document.getElementById("sharingPct").style.display = "none";
        } else if(project_status == "Sharing Project"){
          $("#sharing_project").prop("checked", true);
          document.getElementById("sharingPct").style.display = "block";
        }

        document.getElementById("sharing_pct").value = response["selectedProjectDetails"]["sharing_pct"];

        //LAND AREA
        landarea = response["selectedProjectDetails"]["landarea"];
        var length = document.getElementsByClassName("fs2").length;
        $("#fs2-fields").val(length);

        for(var i=0; i< landarea.length -1; i++){
          if(length != landarea.length){          
            addRow(undefined, "fs2");
          }
        }
        
        for(var i=0; i<landarea.length; i++){          
          $("#fs2-" + i + "-mouza").val(landarea[i]["mouza"]);
          $("#fs2-" + i + "-khata_no").val(landarea[i]["khata_no"]);
          $("#fs2-" + i + "-plot_no").val(landarea[i]["plot_no"]);
          $("#fs2-" + i + "-kisam").val(landarea[i]["kisam"]);
          $("#fs2-" + i + "-area").val(landarea[i]["area"]);
          $("#fs2-" + i + "-rent_receipt_fyr").val(landarea[i]["rent_receipt_fyr"]);
        }

        totalArea();
        // End LAND AREA

        document.getElementById("devAuth_approval_no").value = response["selectedProjectDetails"]["devAuth_approval_no"];
        document.getElementById("devAuth_approval_fromdate").value = formatDate(response["selectedProjectDetails"]["devAuth_approval_fromdate"]);
        document.getElementById("devAuth_approval_todate").value =formatDate(response["selectedProjectDetails"]["devAuth_approval_todate"]);
        document.getElementById("renewal_devAuth_approval_no").value = response["selectedProjectDetails"]["renewal_devAuth_approval_no"];
        document.getElementById("renewal_devAuth_approval_fromdate").value = formatDate(response["selectedProjectDetails"]["renewal_devAuth_approval_fromdate"]);
        document.getElementById("renewal_devAuth_approval_todate").value = formatDate(response["selectedProjectDetails"]["renewal_devAuth_approval_todate"]);
        document.getElementById("rera_certificate_no").value = response["selectedProjectDetails"]["rera_certificate_no"];
        document.getElementById("rera_certificate_fromdate").value = formatDate(response["selectedProjectDetails"]["rera_certificate_fromdate"]);
        document.getElementById("rera_certificate_todate").value = formatDate(response["selectedProjectDetails"]["rera_certificate_todate"]);
        document.getElementById("renewal_rera_certificate_no").value = response["selectedProjectDetails"]["renewal_rera_certificate_no"];
        document.getElementById("renewal_rera_certificate_fromdate").value = formatDate(response["selectedProjectDetails"]["renewal_rera_certificate_fromdate"]);
        document.getElementById("renewal_rera_certificate_todate").value = formatDate(response["selectedProjectDetails"]["renewal_rera_certificate_todate"]);

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
        var _id = response["selectedBlockDetails"]["_id"];
        document.getElementById("_id").value = _id;
        document.getElementById("project_name").value = response["selectedBlockDetails"]["project_name"];
        document.getElementById("no_blocks").value = response["selectedBlockDetails"]["no_blocks"];

        //BLOCKS
        blocks = response["selectedBlockDetails"]["blocks"];
        var length = document.getElementsByClassName("fs1").length;
        $("#fs1-fields").val(length);

        no_blocks = Number(response["selectedBlockDetails"]["no_blocks"]);
        for(var i=0; i< no_blocks -1; i++){
          if(length != blocks.length){          
            addRow(undefined, "fs1");
          }
        }
        
        for(var i=0; i<blocks.length; i++){          
          $("#fs1-" + i + "-block_name").val(blocks[i]["block_name"]);  
          
          $("#fs1-" + i + "-no_floors").val(blocks[i]["no_floors"]);
          document.getElementById("fs1-" + i + "-no_floors").dispatchEvent(new Event('focusout')); 

          $("#fs1-" + i + "-floor_no").val(blocks[i]["floor_no"]);
          $("#fs1-" + i + "-no_flats").val(blocks[i]["no_flats"]);
        }
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
        var _id = response["selectedFlatDetails"]["_id"];
        document.getElementById("_id").value = _id;
        $("#project_name").val(response["selectedFlatDetails"]["project_name"]).change();
        $("#block_name").val(response["selectedFlatDetails"]["block_name"]).change();
        document.getElementById("floor_no").value = response["selectedFlatDetails"]["floor_no"];

        //FLATS
        flats = response["selectedFlatDetails"]["flats"];
        var length = document.getElementsByClassName("fs1").length;
        $("#fs1-fields").val(length);

        for(var i=0; i< flats.length -1; i++){
          if(length != flats.length){          
            addRow(undefined, "fs1");
          }
        }
        
        for(var i=0; i<flats.length; i++){          
          $("#fs1-" + i + "-flat_no").val(flats[i]["flat_no"]);
          $("#fs1-" + i + "-flat_type").val(flats[i]["flat_type"]);
          $("#fs1-" + i + "-ownership_status").val(flats[i]["ownership_status"]);
          $("#fs1-" + i + "-flat_status").val(flats[i]["flat_status"]);
          $("#fs1-" + i + "-carpet_area").val(flats[i]["carpet_area"]).change();
          $("#fs1-" + i + "-builtup_area").val(flats[i]["builtup_area"]).change();
          $("#fs1-" + i + "-superbuiltup_area").val(flats[i]["superbuiltup_area"]).change();
          $("#fs1-" + i + "-parking_no").val(flats[i]["parking_no"]);
          $("#fs1-" + i + "-parking_area").val(flats[i]["parking_area"]);
        }
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
        document.getElementById("customer_dob").value = formatDate(response["selectedCustomerDetails"]["customer_dob"]);
        document.getElementById("customer_gender").value = response["selectedCustomerDetails"]["customer_gender"];
        document.getElementById("customer_occupation").value = response["selectedCustomerDetails"]["customer_occupation"];
        document.getElementById("customer_employer_company_name").value = response["selectedCustomerDetails"]["customer_employer_company_name"];
        document.getElementById("customer_company_address").value = response["selectedCustomerDetails"]["customer_company_address"];
        document.getElementById("customer_posted_at").value = response["selectedCustomerDetails"]["customer_posted_at"];       
        document.getElementById("customer_caste").value = response["selectedCustomerDetails"]["customer_caste"];

        document.getElementById("co-owner_salutation").value = response["selectedCustomerDetails"]["co-owner_salutation"];
        document.getElementById("co-owner_fname").value = response["selectedCustomerDetails"]["co-owner_fname"];
        document.getElementById("co-owner_mname").value = response["selectedCustomerDetails"]["co-owner_mname"];
        document.getElementById("co-owner_lname").value = response["selectedCustomerDetails"]["co-owner_lname"];
        document.getElementById("co-owner_dob").value = formatDate(response["selectedCustomerDetails"]["co-owner_dob"]);
        document.getElementById("co-owner_gender").value = response["selectedCustomerDetails"]["co-owner_gender"];
        document.getElementById("co-owner_occupation").value = response["selectedCustomerDetails"]["co-owner_occupation"];
        document.getElementById("co-owner_employer_company_name").value = response["selectedCustomerDetails"]["co-owner_employer_company_name"];
        document.getElementById("co-owner_company_address").value = response["selectedCustomerDetails"]["co-owner_company_address"];
        document.getElementById("co-owner_posted_at").value = response["selectedCustomerDetails"]["co-owner_posted_at"];     
        document.getElementById("co-owner_caste").value = response["selectedCustomerDetails"]["co-owner_caste"];
        document.getElementById("co-owner_relation").value = response["selectedCustomerDetails"]["co-owner_relation"];

        document.getElementById("email").value = response["selectedCustomerDetails"]["email"];
        document.getElementById("mobile_no").value = response["selectedCustomerDetails"]["mobile_no"];
        document.getElementById("whatsapp_no").value = response["selectedCustomerDetails"]["whatsapp_no"];
  
        document.getElementById("father_husband's_salutation").value = response["selectedCustomerDetails"]["father_husband's_salutation"];
        document.getElementById("father_husband's_name").value = response["selectedCustomerDetails"]["father_husband's_name"];
        document.getElementById("relation").value = response["selectedCustomerDetails"]["relation"];

        document.getElementById("copy_from").value = response["selectedCustomerDetails"]["copy_from"];
        document.getElementById("contact_p_salutation").value = response["selectedCustomerDetails"]["contact_p_salutation"];
        document.getElementById("contact_p_name").value = response["selectedCustomerDetails"]["contact_p_name"];
        document.getElementById("contact_p_phone_no").value = response["selectedCustomerDetails"]["contact_p_phone_no"];

        copy_present = response["selectedCustomerDetails"]["copy_present"];
        if(copy_present == "copy_present"){
          document.getElementById("copy_present").checked = true;
        } else{
          document.getElementById("copy_present").checked = false;
        }

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

        document.getElementById("username").value = response["selectedCustomerDetails"]["username"];
        document.getElementById("password").value = response["selectedCustomerDetails"]["password"];

        document.getElementById("bank_name").value = response["selectedCustomerDetails"]["bank_name"];
        document.getElementById("branch_name").value = response["selectedCustomerDetails"]["branch_name"];
        document.getElementById("branch_address").value = response["selectedCustomerDetails"]["branch_address"];
        document.getElementById("branch_city").value = response["selectedCustomerDetails"]["branch_city"];
        document.getElementById("ifsc_code").value = response["selectedCustomerDetails"]["ifsc_code"];
        document.getElementById("account_type").value = response["selectedCustomerDetails"]["account_type"];
        document.getElementById("account_no").value = response["selectedCustomerDetails"]["account_no"];

        document.getElementById("aadhar_no").value = response["selectedCustomerDetails"]["aadhar_no"];
        document.getElementById("pan_no").value = response["selectedCustomerDetails"]["pan_no"];
        document.getElementById("voter_id").value = response["selectedCustomerDetails"]["voter_id"];
        document.getElementById("gst_no").value = response["selectedCustomerDetails"]["gst_no"];
        document.getElementById("broker_pan_no").value = response["selectedCustomerDetails"]["broker's_pan_no"];

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
        var _id = response["selectedBankDetails"]["_id"];
        document.getElementById("_id").value = _id;
        document.getElementById("bank_name").value = response["selectedBankDetails"]["bank_name"];
        document.getElementById("short_bank_name").value = response["selectedBankDetails"]["short_bank_name"];
        document.getElementById("branch").value = response["selectedBankDetails"]["branch"];
        document.getElementById("address").value = response["selectedBankDetails"]["address"];
        document.getElementById("pin_code").value = response["selectedBankDetails"]["pin_code"];
        document.getElementById("branch_manager").value = response["selectedBankDetails"]["branch_manager"];
        document.getElementById("branch_manager_phno").value = response["selectedBankDetails"]["branch_manager_phno"];
        document.getElementById("contact_person").value = response["selectedBankDetails"]["contact_person"];
        document.getElementById("contact_person_phno").value = response["selectedBankDetails"]["contact_person_phno"];
        document.getElementById("ifsc_code").value = response["selectedBankDetails"]["ifsc_code"];
        document.getElementById("rate_of_interest").value = response["selectedBankDetails"]["rate_of_interest"];

        projects = ""
        approved_projects = response["selectedBankDetails"]["approved_projects"];
        for (var i=0; i<approved_projects.length; i++){
          projects += approved_projects[i]["project_name"] + ",";
        }
        document.getElementById("approved_projects").value = projects;

        showFiles("Master", "Bank", response["files"]);
      },
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";   
}

function showBrokerData(_url){
  show_modal()
  if(_url != undefined && _url.length > 0){
    $.ajax({      
      url: _url,
      enctype: 'multipart/form-data',    
      success: function(response){
        var _id = response["selectedBrokerDetails"]["_id"];
        document.getElementById("_id").value = _id;
        document.getElementById("broker_salutation").value = response["selectedBrokerDetails"]["broker_salutation"];
        document.getElementById("broker_name").value = response["selectedBrokerDetails"]["broker_name"];
        document.getElementById("broker_address").value = response["selectedBrokerDetails"]["broker_address"];
        document.getElementById("broker_phno").value = response["selectedBrokerDetails"]["broker_phno"];
        document.getElementById("brokerage_commission").value = response["selectedBrokerDetails"]["brokerage_commission"];
        
        document.getElementById("aadhar_no").value = response["selectedBrokerDetails"]["aadhar_no"];
        document.getElementById("pan_no").value = response["selectedBrokerDetails"]["pan_no"];
        document.getElementById("gst_no").value = response["selectedBrokerDetails"]["gst_no"];

        showFiles("Master", "Broker", response["files"]);
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
        var _id = response["selectedBookingEntry"]["_id"];
        document.getElementById("_id").value = _id;
        document.getElementById("reference_id").value = response["selectedBookingEntry"]["reference_id"];
        document.getElementById("booking_date").value = formatDate(response["selectedBookingEntry"]["booking_date"]);
        $("#customer_name").val(response["selectedBookingEntry"]["customer_name"]).change();
        
        ownership_status = response["selectedBookingEntry"]["landowner_company_share"];
        if (ownership_status == "COMPANY SHARE"){
          document.getElementById("company_share").checked = true;
        } else if (ownership_status == "LAND-OWNER SHARE"){
          document.getElementById("land-owner_share").checked = true;
        }
        
        $("#project_name").val(response["selectedBookingEntry"]["project_name"]).change();
        $("#block_name").val(response["selectedBookingEntry"]["block_name"]).change();
        $("#floor_no").val(response["selectedBookingEntry"]["floor_no"]).change();
        $("#flat_no").val(response["selectedBookingEntry"]["flat_no"]).change();
        document.getElementById("flat_condn").value = response["selectedBookingEntry"]["flat_condn"];
        document.getElementById("broker_name").value = response["selectedBookingEntry"]["broker_name"];

        //PAYMENT DETAILS
        payment_details = response["selectedBookingEntry"]["payment_details"];
        var length = document.getElementsByClassName("fs1").length;
        $("#fs1-fields").val(length);

        for(var i=0; i< payment_details.length -1; i++){
          if(length != payment_details.length){          
            addRow(undefined, "fs1");
          }
        }
        
        for(var i=0; i<payment_details.length; i++){          
          $("#fs1-" + i + "-payment_date").val(formatDate(payment_details[i]["payment_date"]));
          $("#fs1-" + i + "-payment_mode").val(payment_details[i]["payment_mode"]);
          $("#fs1-" + i + "-payment_details").val(payment_details[i]["payment_details"]);
          $("#fs1-" + i + "-bank_name").val(payment_details[i]["bank_name"]);
          $("#fs1-" + i + "-amount").val(payment_details[i]["amount"]).change();
        }

        document.getElementById("sellable_area").value = response["selectedBookingEntry"]["sellable_area"];
        document.getElementById("sellable_area_rate").value = response["selectedBookingEntry"]["sellable_area_rate"];
        document.getElementById("sellable_area_amount").value = response["selectedBookingEntry"]["sellable_area_amount"];
        $("#car_parking_chgs").val(response["selectedBookingEntry"]["car_parking_chgs"]).change();
        $("#dg_chgs").val(response["selectedBookingEntry"]["dg_chgs"]).change();
        $("#trans_substation_chgs").val(response["selectedBookingEntry"]["trans_substation_chgs"]).change();
        $("#discount").val(response["selectedBookingEntry"]["discount"]).change();
        $("#cash_discount").val(response["selectedBookingEntry"]["cash_discount"]).change();
        $("#add_gst_pct").val(response["selectedBookingEntry"]["add_gst_pct"]).change();
        document.getElementById("less_booking_amount").value = response["selectedBookingEntry"]["less_booking_amount"];
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
        var _id = response["selectedCustomerRequest"]["_id"];
        document.getElementById("_id").value = _id;
        document.getElementById("request_date").value = response["selectedCustomerRequest"]["request_date"];
        document.getElementById("customer_salutation").value = response["selectedCustomerRequest"]["customer_salutation"];
        document.getElementById("customer_fname").value = response["selectedCustomerRequest"]["customer_fname"];
        document.getElementById("customer_mname").value = response["selectedCustomerRequest"]["customer_mname"];
        document.getElementById("customer_lname").value = response["selectedCustomerRequest"]["customer_lname"];
        document.getElementById("customer_dob").value = response["selectedCustomerRequest"]["customer_dob"];
        document.getElementById("customer_gender").value = response["selectedCustomerRequest"]["customer_gender"];
        document.getElementById("mobile_no").value = response["selectedCustomerRequest"]["mobile_no"];
        document.getElementById("whatsapp_no").value = response["selectedCustomerRequest"]["whatsapp_no"];
        document.getElementById("email").value = response["selectedCustomerRequest"]["email"];
        document.getElementById("occupation").value = response["selectedCustomerRequest"]["occupation"];
        document.getElementById("contact_p_salutation").value = response["selectedCustomerRequest"]["contact_p_salutation"];
        document.getElementById("contact_p_name").value = response["selectedCustomerRequest"]["contact_p_name"];
        document.getElementById("contact_p_phone_no").value = response["selectedCustomerRequest"]["contact_p_phone_no"];
        document.getElementById("pr_addLine1").value = response["selectedCustomerRequest"]["pr_addLine1"];
        document.getElementById("pr_addLine2").value = response["selectedCustomerRequest"]["pr_addLine2"];
        document.getElementById("pr_city").value = response["selectedCustomerRequest"]["pr_city"];
        document.getElementById("pr_state").value = response["selectedCustomerRequest"]["pr_state"];
        document.getElementById("pr_pincode").value = response["selectedCustomerRequest"]["pr_pincode"];
        document.getElementById("project_name").value = response["selectedCustomerRequest"]["project_name"];
        document.getElementById("block_name").value = response["selectedCustomerRequest"]["block_name"];
        document.getElementById("floor_no").value = response["selectedCustomerRequest"]["floor_no"];
        document.getElementById("flat_no").value = response["selectedCustomerRequest"]["flat_no"];
        document.getElementById("to_be_hold_days").value = response["selectedCustomerRequest"]["to_be_hold_days"];
        document.getElementById("status").value = response["selectedCustomerRequest"]["status"];
        document.getElementById("reason_of_unhold").value = response["selectedCustomerRequest"]["reason_of_unhold"];
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
        var _id = response["selectedUserDetails"]["_id"];
        document.getElementById("_id").value = _id;
        document.getElementById("username").value = response["selectedUserDetails"]["username"];
        document.getElementById("password").value = response["selectedUserDetails"]["password"];
        document.getElementById("user_type").value = response["selectedUserDetails"]["user_type"];
        document.getElementById("full_name").value = response["selectedUserDetails"]["full_name"];
        document.getElementById("designation").value = response["selectedUserDetails"]["designation"];
      },
      error: function(error) {
        console.log(error)
      }
    });
  }
  document.getElementById("btn").value = "Update";
  document.getElementById("btn").name = "Update";   
}