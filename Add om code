function buildAddOn(e) 
{

  var accessToken = e.messageMetadata.accessToken;
  GmailApp.setCurrentMessageAccessToken(accessToken);

  var messageId = e.messageMetadata.messageId;
  var message = GmailApp.getMessageById(messageId);
  var sender = message.getFrom();

  var email=sender.split("<")[1].split(">")[0];

  var body = message.getPlainBody();
//  var data_send={'content':body};
//  var options = {
//  'method' : 'post',
//  'contentType': 'application/json',
//  // Convert the JavaScript object to a JSON string.
//  'payload' : JSON.stringify(data_send)
//};
    paramms = {"content" : body }
    var options = 
        {
          "method" : "POST",
          "contentType" : "application/json",
          "payload" :  JSON.stringify(paramms),
          "muteHttpExceptions" : true
          
        };

var response = UrlFetchApp.fetch('https://instavans-gmailaddon.herokuapp.com/post',options);
  console.log("check for response###",response.getContentText());
  
  console.log(response.getContentText());
  var data_main = JSON.parse(response);
  var data =data_main["main"];
  console.log("data is ", data)
  var date=data_main["date"];
  var mobile = data_main["mobile"]
  console.log(mobile);
  console.log(date);
  console.log(data.length);
  console.log(data);
  
  
  
  console.log(" himmat is there",body);

  var card = CardService.newCardBuilder();
  var suggest=["himmat","ripul","rishab","ramesh"];
  var demoSection=CardService.newCardSection().setHeader('<b><font color="#4285F4">CLIENT</font></b>');
  demoSection.addWidget(CardService.newTextInput().setSuggestions(CardService.newSuggestions().addSuggestions(suggest)).setFieldName("organisation").setTitle("Unit").setValue(""));
  
  
  var section = CardService.newCardSection().setHeader('<b><font color="#4285F4">PERSONAL DETAILS</font></b>')
  
  var section2 = CardService.newCardSection().setHeader('<b><font color="#4285F4">DROP ADDRESS</font></b>');
  
  var section3 = CardService.newCardSection();
  var action1 = CardService.newAction().setFunctionName('placeOrder');

  var action2 = CardService.newAction().setFunctionName('changeValue2');
  section.addWidget(CardService.newTextInput().setFieldName("username").setTitle("Username").setValue(message.getFrom())).setCollapsible(true);
  section.addWidget(CardService.newTextInput().setFieldName("emailId").setTitle("emailId").setValue(email)).setCollapsible(true);

  for(var mob = 0; mob<mobile.length; mob++)
  {
    var string = "mobile"+(mob+1);
    section.addWidget(CardService.newTextInput().setFieldName(string).setTitle("Mobile No.").setValue(mobile[mob])).setCollapsible(true);
  }
  section.addWidget(CardService.newTextInput().setFieldName("date").setTitle("Date").setValue(date[0]))
  card.addSection(section).build();
  card.addSection(demoSection).build();
  var sec= new Array(data.length);
  var i
  console.log("length of data is ", data.length);
  for(i=0;i<data.length;i++)
  {
    sec[i]= CardService.newCardSection().setHeader('<b><font color="#4285F4">ORDER </font></b>'+'<b><font color="#4285F4">'+(i+1)+ '</font></b>');
    
    
    for(var v=0 ;v<data[i].vehicle.length ;v++)
    {
      var d=[false,false,false,false,false,false,false,false,false]
      var veh_type=["tata ace","tata super ace","tata 407","canter 14","canter 17","canter 19","canter 20","bolero","dost"];
      var val = data[i].vehicle[v];
      for(var vt=0;vt<veh_type.length;vt++)
      {
        if(val==veh_type[vt])
        {
          d[vt]=true;
        }
      }
      var string = "vehicle_type$"+(i+1)+"@"+(v+1);
      var dropdown=CardService.newSelectionInput()
    .setType(CardService.SelectionInputType.DROPDOWN)
    .setTitle("Vehicle").setFieldName(string)
    .addItem("Tata Ace", "tata ace", d[0])
    .addItem("Tata Super Ace", "tata super ace", d[1])
      .addItem("tata 407", "tata 407", d[2])
      .addItem("canter 14","canter 14", d[3])
      .addItem("canter 17","canter 17", d[4])
      .addItem("canter 19","canter 19", d[5])
      .addItem("canter 20","canter 20", d[6])
      .addItem("Bolero","bolero", d[7])
      .addItem("Dost","dost", d[8])
      
    sec[i].addWidget(dropdown);
    }
       var action7 = CardService.newAction().setFunctionName('addvehicle').setParameters({"ind":""+(i+1)});
      var action8= CardService.newAction().setFunctionName('removevehicle').setParameters({"ind":""+(i+1)});
      var TextButton7= CardService.newTextButton().setText('+vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action7);
      var TextButton8 =CardService.newTextButton().setText('-vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action8);
      
      var Buttonset4vehicle = CardService.newButtonSet().addButton(TextButton7).addButton(TextButton8)
      sec[i].addWidget(Buttonset4vehicle);
    //end of vehicle 
    for(var index in data[i])
    {
      console.log("index is ", index);
      if(index=="pickup")
    {
      for(var j=0;j<data[i][index].length;j++)
      {
        console.log("print the pickup length", data[i][index][j]);
        var ind =j+1;
        var string ="pickup$"+(i+1)+"@"+ind;
        var name ="pickup "+ind;
        sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setValue(data[i][index][j]));
      }
      var action3 = CardService.newAction().setFunctionName('addpickup').setParameters({"ind":""+(i+1)});
      var action6= CardService.newAction().setFunctionName('removepickup').setParameters({"ind":""+(i+1)});
      var TextButton3= CardService.newTextButton().setText('+PickUp')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action3);
      var TextButton32 =CardService.newTextButton().setText('-pickup')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action6);
      
      var Buttonset4pickup = CardService.newButtonSet().addButton(TextButton3).addButton(TextButton32)
      
      sec[i].addWidget(Buttonset4pickup);
      
      
    }
    }
    for(var index in data[i]){
      if(index=="drop")
      {
        for(var j=0;j<data[i][index].length;j++)
        {
          var string ="drop$"+(i+1)+"@"+(j+1);
          var name ="drop "+(j+1);
          var t=CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(data[i][index][j]);
         
          sec[i].addWidget(t);
         
        }
      
        var action4 = CardService.newAction().setFunctionName('adddrop').setParameters({"ind" : ""+(i+1)});
        var action5 = CardService.newAction().setFunctionName('removedrop').setParameters({"ind" : ""+(i+1)});
        var TextButton4= CardService.newTextButton().setText('+drop')
        .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action4);
      var TextButton42=CardService.newTextButton().setText('-drop')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action5);
      
        var Buttonset4drop=CardService.newButtonSet().addButton(TextButton4).addButton(TextButton42);
        
        sec[i].addWidget(Buttonset4drop);

      
        
      }
      
      
    }
    
    card.addSection(sec[i]).build();
  }
  var TextButton2= CardService.newTextButton().setText('place Order')
  .setBackgroundColor("#E54131").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
  .setOnClickAction(action1);
  
  var Buttonset =CardService.newButtonSet().addButton(TextButton2)
  section3.addWidget(Buttonset)
  
  return card.addSection(section3).build();
 
}



function changeValue2()
{ 
}





function addpickup(e)
{
  
  var accessToken = e.messageMetadata.accessToken;
  GmailApp.setCurrentMessageAccessToken(accessToken);

  var messageId = e.messageMetadata.messageId;
  var message = GmailApp.getMessageById(messageId);
  var sender = message.getFrom();

  var email=sender.split("<")[1].split(">")[0];

  var body = message.getPlainBody();
  
  console.log(body);
  
  var parameter = e.parameters;
  var final = parameter["ind"];
      paramms = {"content" : body }
    var options = 
        {
          "method" : "POST",
          "contentType" : "application/json",
          "payload" :  JSON.stringify(paramms),
          "muteHttpExceptions" : true
          
        };
  
  var response = UrlFetchApp.fetch('https://instavans-gmailaddon.herokuapp.com/post',options);
  var data_main = JSON.parse(response);
  var data =data_main["main"];
  var date=data_main["date"];
  var mobile = data_main["mobile"]
  
  
  updated_data=e.formInput;
  console.log("pickup is ", e.formInput);
  var p = new Array(data.length);
  var d = new Array(data.length);
  var v = new Array(data.length);
  for(var i =0;i<data.length; i++)
  {
    p[i]=0;
    d[i]=0;
    v[i]=0;
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0]=="vehicle_type")
      {
        var temp =key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        
        if(max>v[temp-1])
        {
          v[temp-1]=max;
          console.log("v[temp-1] is ",temp-1,"is ",v[temp-1]);
        }
      }
    }
  }
  
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "pickup")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("max is " , typeof(max))
        if(max>p[temp-1])
        {
          p[temp-1]=max;;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "drop")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("drop max is " , max)
        if(max>d[temp-1])
        {
          d[temp-1]=max;
        }
      }
    }
  }
  for(var i =0;i<data.length; i++)
  {
    console.log("p[i]",p[i]," d[i] ", d[i], "v[i] ",v[i]);
  }
  
   var card = CardService.newCardBuilder();
  

  
  var section = CardService.newCardSection().setHeader('<b><font color="#4285F4">PERSONAL DETAILS</font></b>')
  
  var section2 = CardService.newCardSection().setHeader('<b><font color="#4285F4">DROP ADDRESS</font></b>');
  
  var section3 = CardService.newCardSection();
  var action1 = CardService.newAction().setFunctionName('placeOrder');

  var action2 = CardService.newAction().setFunctionName('changeValue2');
  section.addWidget(CardService.newTextInput().setFieldName("username").setTitle("Username").setValue(message.getFrom())).setCollapsible(true);
  section.addWidget(CardService.newTextInput().setFieldName("emailId").setTitle("emailId").setValue(email)).setCollapsible(true);
  for(var mob = 0; mob<mobile.length; mob++)
  {
    var string = "mobile"+(mob+1);
    section.addWidget(CardService.newTextInput().setFieldName(string).setTitle("Mobile No.").setValue(mobile[mob])).setCollapsible(true);
  }
  section.addWidget(CardService.newTextInput().setFieldName("date").setTitle("Date").setValue(date[0]))
  card.addSection(section).build();
  //update right now
  
  var sec = new Array(data.length);

  
  for(var i=0;i<data.length;i++)
  {
    
    sec[i]= CardService.newCardSection().setHeader('<b><font color="#4285F4">ORDER </font></b>'+'<b><font color="#4285F4">'+(i+1)+ '</font></b>');
//    var string = "vehicle_type$"+(i+1);
//    sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle("Vehicle").setValue(data[i].vehicle_type));
    
    for(var x=0 ;x<v[i];x++)
    {
      var string = "vehicle_type$"+(i+1)+"@"+(x+1);
      var name = "vehicle "+(x+1);
      //enter here vevery thing related to vehicle
      var tf=[false,false,false,false,false,false,false,false,false]
      var veh_type=["tata ace","tata super ace","tata 407","canter 14","canter 17","canter 19","canter 20","bolero","dost"];
      var val = updated_data[string];
      for(var vt=0;vt<veh_type.length;vt++)
      {
        if(val==veh_type[vt])
        {
          tf[vt]=true;
        }
      }
//      var string = "vehicle_type$"+(i+1)+"@"+(v+1);
      var dropdown=CardService.newSelectionInput()
    .setType(CardService.SelectionInputType.DROPDOWN)
    .setTitle(name).setFieldName(string)
    .addItem("Tata Ace", "tata ace", tf[0])
    .addItem("Tata Super Ace", "tata super ace", tf[1])
      .addItem("tata 407", "tata 407", tf[2])
      .addItem("canter 14","canter 14", tf[3])
      .addItem("canter 17","canter 17", tf[4])
      .addItem("canter 19","canter 19", tf[5])
      .addItem("canter 20","canter 20", tf[6])
      .addItem("Bolero","bolero", tf[7])
      .addItem("Dost","dost", tf[8])
      
    sec[i].addWidget(dropdown);
      
    }
    
      var action7 = CardService.newAction().setFunctionName('addvehicle').setParameters({"ind":""+(i+1)});
      var action8= CardService.newAction().setFunctionName('removevehicle').setParameters({"ind":""+(i+1)});
      var TextButton7= CardService.newTextButton().setText('+vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action7);
      var TextButton8 =CardService.newTextButton().setText('-vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action8);
      
      var Buttonset4vehicle = CardService.newButtonSet().addButton(TextButton7).addButton(TextButton8)
      sec[i].addWidget(Buttonset4vehicle);
    
    for(var j=0;j<p[i];j++)
    {
      var string= "pickup$"+(i+1)+"@"+(j+1);
      var name ="pickup "+(j+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
  if((i+1)==final)
  {
    string = "pickup$"+(i+1)+"@"+(p[i]+1);
    name="pickup "+(p[i]+1);
    sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(" "))
  }
    
      var action3 = CardService.newAction().setFunctionName('addpickup').setParameters({"ind":""+(i+1)});
      var action6= CardService.newAction().setFunctionName('removepickup').setParameters({"ind":""+(i+1)});
      var TextButton3= CardService.newTextButton().setText('+PickUp')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action3);
      var TextButton32 =CardService.newTextButton().setText('-pickup')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action6);
      
      var Buttonset4pickup = CardService.newButtonSet().addButton(TextButton3).addButton(TextButton32)
      
      sec[i].addWidget(Buttonset4pickup);
    
    for(var k=0;k<d[i];k++){
      string ="drop$"+(i+1)+"@"+(k+1);
      name="drop "+(k+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
        var action4 = CardService.newAction().setFunctionName('adddrop').setParameters({"ind" : ""+(i+1)});
        var action5 = CardService.newAction().setFunctionName('removedrop').setParameters({"ind" : ""+(i+1)});
        var TextButton4= CardService.newTextButton().setText('+drop')
        .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action4);
      var TextButton42=CardService.newTextButton().setText('-drop')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action5);
      
        var Buttonset4drop=CardService.newButtonSet().addButton(TextButton4).addButton(TextButton42);
        
        sec[i].addWidget(Buttonset4drop);

      
        card.addSection(sec[i]).build();
    
    
    
  }
  
    var TextButton2= CardService.newTextButton().setText('place Order')
  .setBackgroundColor("#E54131").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
  .setOnClickAction(action1);
  
  var Buttonset =CardService.newButtonSet().addButton(TextButton2)
  section3.addWidget(Buttonset)
  
  card.addSection(section3).build();
  
  return CardService.newNavigation().updateCard(card.build());
}

  
  
 

function adddrop(e){
  
  var accessToken = e.messageMetadata.accessToken;
  GmailApp.setCurrentMessageAccessToken(accessToken);

  var messageId = e.messageMetadata.messageId;
  var message = GmailApp.getMessageById(messageId);
  var sender = message.getFrom();

  var email=sender.split("<")[1].split(">")[0];

  var body = message.getPlainBody();
  
  console.log(body);
  
  var parameter = e.parameters;
  var final = parameter["ind"];
  paramms = {"content" : body }
    var options = 
        {
          "method" : "POST",
          "contentType" : "application/json",
          "payload" :  JSON.stringify(paramms),
          "muteHttpExceptions" : true
          
        };
  
  var response = UrlFetchApp.fetch('https://instavans-gmailaddon.herokuapp.com/post',options);
  var data_main = JSON.parse(response);
  var data =data_main["main"];
  var date=data_main["date"];
  var mobile = data_main["mobile"]
  
  
  updated_data=e.formInput;
  console.log("pickup is ", e.formInput);
  var p = new Array(data.length);
  var d = new Array(data.length);
  var v = new Array(data.length);
  for(var i =0;i<data.length; i++)
  {
    p[i]=0;
    d[i]=0;
    v[i]=0;
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0]=="vehicle_type")
      {
        var temp =key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        
        if(max>v[temp-1])
        {
          v[temp-1]=max;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "pickup")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("max is " , typeof(max))
        if(max>p[temp-1])
        {
          p[temp-1]=max;;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "drop")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("drop max is " , max)
        if(max>d[temp-1])
        {
          d[temp-1]=max;
        }
      }
    }
  }
  for(var i =0;i<data.length; i++)
  {
    console.log("p[i]",typeof(p[i])," d[i] ", d[i], "v[i] ",v[i]);
  }
  
   var card = CardService.newCardBuilder();
  

  
  var section = CardService.newCardSection().setHeader('<b><font color="#4285F4">PERSONAL DETAILS</font></b>')
  
  var section2 = CardService.newCardSection().setHeader('<b><font color="#4285F4">DROP ADDRESS</font></b>');
  
  var section3 = CardService.newCardSection();
  var action1 = CardService.newAction().setFunctionName('placeOrder');

  var action2 = CardService.newAction().setFunctionName('changeValue2');
  section.addWidget(CardService.newTextInput().setFieldName("username").setTitle("Username").setValue(message.getFrom())).setCollapsible(true);
  section.addWidget(CardService.newTextInput().setFieldName("emailId").setTitle("emailId").setValue(email)).setCollapsible(true);
  for(var mob = 0; mob<mobile.length; mob++)
  {
    var string = "mobile"+(mob+1);
    section.addWidget(CardService.newTextInput().setFieldName(string).setTitle("Mobile No.").setValue(mobile[mob])).setCollapsible(true);
  }
  section.addWidget(CardService.newTextInput().setFieldName("date").setTitle("Date").setValue(date[0]))
  card.addSection(section).build();
  //update right now
  
  var sec = new Array(data.length);

  
  for(var i=0;i<data.length;i++)
  {
    
    sec[i]= CardService.newCardSection().setHeader('<b><font color="#4285F4">ORDER </font></b>'+'<b><font color="#4285F4">'+(i+1)+ '</font></b>');
//    var string = "vehicle_type$"+(i+1);
//    sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle("Vehicle").setValue(data[i].vehicle_type));
    
    for(var x=0 ;x<v[i];x++)
    {
      var string = "vehicle_type$"+(i+1)+"@"+(x+1);
      var name = "vehicle "+(x+1);
      //enter here vevery thing related to vehicle
      var tf=[false,false,false,false,false,false,false,false,false]
      var veh_type=["tata ace","tata super ace","tata 407","canter 14","canter 17","canter 19","canter 20","bolero","dost"];
      var val = updated_data[string];
      for(var vt=0;vt<veh_type.length;vt++)
      {
        if(val==veh_type[vt])
        {
          tf[vt]=true;
        }
      }
//      var string = "vehicle_type$"+(i+1)+"@"+(v+1);
      var dropdown=CardService.newSelectionInput()
    .setType(CardService.SelectionInputType.DROPDOWN)
    .setTitle(name).setFieldName(string)
    .addItem("Tata Ace", "tata ace", tf[0])
    .addItem("Tata Super Ace", "tata super ace", tf[1])
      .addItem("tata 407", "tata 407", tf[2])
      .addItem("canter 14","canter 14", tf[3])
      .addItem("canter 17","canter 17", tf[4])
      .addItem("canter 19","canter 19", tf[5])
      .addItem("canter 20","canter 20", tf[6])
      .addItem("Bolero","bolero", tf[7])
      .addItem("Dost","dost", tf[8])
      
    sec[i].addWidget(dropdown);
      
    }
    
      var action7 = CardService.newAction().setFunctionName('addvehicle').setParameters({"ind":""+(i+1)});
      var action8= CardService.newAction().setFunctionName('removevehicle').setParameters({"ind":""+(i+1)});
      var TextButton7= CardService.newTextButton().setText('+vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action7);
      var TextButton8 =CardService.newTextButton().setText('-vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action8);
      
      var Buttonset4vehicle = CardService.newButtonSet().addButton(TextButton7).addButton(TextButton8)
      sec[i].addWidget(Buttonset4vehicle);
    
    for(var j=0;j<p[i];j++)
    {
      var string= "pickup$"+(i+1)+"@"+(j+1);
      var name ="pickup "+(j+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }

    
      var action3 = CardService.newAction().setFunctionName('addpickup').setParameters({"ind":""+(i+1)});
      var action6= CardService.newAction().setFunctionName('removepickup').setParameters({"ind":""+(i+1)});
      var TextButton3= CardService.newTextButton().setText('+PickUp')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action3);
      var TextButton32 =CardService.newTextButton().setText('-pickup')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action6);
      
      var Buttonset4pickup = CardService.newButtonSet().addButton(TextButton3).addButton(TextButton32)
      
      sec[i].addWidget(Buttonset4pickup);
    
    for(var k=0;k<d[i];k++){
      string ="drop$"+(i+1)+"@"+(k+1);
      name="drop "+(k+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
      if((i+1)==final)
  {
    string = "drop$"+(i+1)+"@"+(d[i]+1);
    name="drop "+(d[i]+1);
    sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(" "))
  }
        var action4 = CardService.newAction().setFunctionName('adddrop').setParameters({"ind" : ""+(i+1)});
        var action5 = CardService.newAction().setFunctionName('removedrop').setParameters({"ind" : ""+(i+1)});
        var TextButton4= CardService.newTextButton().setText('+drop')
        .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action4);
      var TextButton42=CardService.newTextButton().setText('-drop')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action5);
      
        var Buttonset4drop=CardService.newButtonSet().addButton(TextButton4).addButton(TextButton42);
        
        sec[i].addWidget(Buttonset4drop);

      
        card.addSection(sec[i]).build();
    
    
    
  }
  
    var TextButton2= CardService.newTextButton().setText('place Order')
  .setBackgroundColor("#E54131").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
  .setOnClickAction(action1);
  
  var Buttonset =CardService.newButtonSet().addButton(TextButton2)
  section3.addWidget(Buttonset)
  
  card.addSection(section3).build();
  
  return CardService.newNavigation().updateCard(card.build());
}



function removepickup(e)
{
  var accessToken = e.messageMetadata.accessToken;
  GmailApp.setCurrentMessageAccessToken(accessToken);

  var messageId = e.messageMetadata.messageId;
  var message = GmailApp.getMessageById(messageId);
  var sender = message.getFrom();

  var email=sender.split("<")[1].split(">")[0];

  var body = message.getPlainBody();
  
  console.log(body);
  
  var parameter = e.parameters;
  var final = parameter["ind"];
  
    paramms = {"content" : body }
    var options = 
        {
          "method" : "POST",
          "contentType" : "application/json",
          "payload" :  JSON.stringify(paramms),
          "muteHttpExceptions" : true
          
        };
  
  var response = UrlFetchApp.fetch('https://instavans-gmailaddon.herokuapp.com/post',options);
  var data_main = JSON.parse(response);
  var data =data_main["main"];
  var date=data_main["date"];
  var mobile = data_main["mobile"]
  
  
  updated_data=e.formInput;
  console.log("pickup is ", e.formInput);
  var p = new Array(data.length);
  var d = new Array(data.length);
  var v = new Array(data.length);
  for(var i =0;i<data.length; i++)
  {
    p[i]=0;
    d[i]=0;
    v[i]=0;
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0]=="vehicle_type")
      {
        var temp =key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        
        if(max>v[temp-1])
        {
          v[temp-1]=max;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "pickup")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("max is " , typeof(max))
        if(max>p[temp-1])
        {
          p[temp-1]=max;;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "drop")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("drop max is " , max)
        if(max>d[temp-1])
        {
          d[temp-1]=max;
        }
      }
    }
  }
  for(var i =0;i<data.length; i++)
  {
    console.log("p[i]",typeof(p[i])," d[i] ", d[i], "v[i] ",v[i]);
  }
  
   var card = CardService.newCardBuilder();
  

  
  var section = CardService.newCardSection().setHeader('<b><font color="#4285F4">PERSONAL DETAILS</font></b>')
  
  var section2 = CardService.newCardSection().setHeader('<b><font color="#4285F4">DROP ADDRESS</font></b>');
  
  var section3 = CardService.newCardSection();
  var action1 = CardService.newAction().setFunctionName('placeOrder');

  var action2 = CardService.newAction().setFunctionName('changeValue2');
  section.addWidget(CardService.newTextInput().setFieldName("username").setTitle("Username").setValue(message.getFrom())).setCollapsible(true);
  section.addWidget(CardService.newTextInput().setFieldName("emailId").setTitle("emailId").setValue(email)).setCollapsible(true);
  for(var mob = 0; mob<mobile.length; mob++)
  {
    var string = "mobile"+(mob+1);
    section.addWidget(CardService.newTextInput().setFieldName(string).setTitle("Mobile No.").setValue(mobile[mob])).setCollapsible(true);
  }
  section.addWidget(CardService.newTextInput().setFieldName("date").setTitle("Date").setValue(date[0]))
  card.addSection(section).build();
  //update right now
  
  var sec = new Array(data.length);

  
  for(var i=0;i<data.length;i++)
  {
    
    sec[i]= CardService.newCardSection().setHeader('<b><font color="#4285F4">ORDER </font></b>'+'<b><font color="#4285F4">'+(i+1)+ '</font></b>');
//    var string = "vehicle_type$"+(i+1);
//    sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle("Vehicle").setValue(data[i].vehicle_type));
    
    for(var x=0 ;x<v[i];x++)
    {
      var string = "vehicle_type$"+(i+1)+"@"+(x+1);
      var name = "vehicle "+(x+1);
      //enter here vevery thing related to vehicle
      var tf=[false,false,false,false,false,false,false,false,false]
      var veh_type=["tata ace","tata super ace","tata 407","canter 14","canter 17","canter 19","canter 20","bolero","dost"];
      var val = updated_data[string];
      for(var vt=0;vt<veh_type.length;vt++)
      {
        if(val==veh_type[vt])
        {
          tf[vt]=true;
        }
      }
//      var string = "vehicle_type$"+(i+1)+"@"+(v+1);
      var dropdown=CardService.newSelectionInput()
    .setType(CardService.SelectionInputType.DROPDOWN)
    .setTitle(name).setFieldName(string)
    .addItem("Tata Ace", "tata ace", tf[0])
    .addItem("Tata Super Ace", "tata super ace", tf[1])
      .addItem("tata 407", "tata 407", tf[2])
      .addItem("canter 14","canter 14", tf[3])
      .addItem("canter 17","canter 17", tf[4])
      .addItem("canter 19","canter 19", tf[5])
      .addItem("canter 20","canter 20", tf[6])
      .addItem("Bolero","bolero", tf[7])
      .addItem("Dost","dost", tf[8])
      
    sec[i].addWidget(dropdown);
      
    }
    
      var action7 = CardService.newAction().setFunctionName('addvehicle').setParameters({"ind":""+(i+1)});
      var action8= CardService.newAction().setFunctionName('removevehicle').setParameters({"ind":""+(i+1)});
      var TextButton7= CardService.newTextButton().setText('+vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action7);
      var TextButton8 =CardService.newTextButton().setText('-vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action8);
      
      var Buttonset4vehicle = CardService.newButtonSet().addButton(TextButton7).addButton(TextButton8)
      sec[i].addWidget(Buttonset4vehicle);
    if((i+1)==final)
  {
    p[i]=p[i]-1;
  }
    for(var j=0;j<p[i];j++)
    {
      var string= "pickup$"+(i+1)+"@"+(j+1);
      var name ="pickup "+(j+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
  
    
      var action3 = CardService.newAction().setFunctionName('addpickup').setParameters({"ind":""+(i+1)});
      var action6= CardService.newAction().setFunctionName('removepickup').setParameters({"ind":""+(i+1)});
      var TextButton3= CardService.newTextButton().setText('+PickUp')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action3);
      var TextButton32 =CardService.newTextButton().setText('-pickup')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action6);
      
      var Buttonset4pickup = CardService.newButtonSet().addButton(TextButton3).addButton(TextButton32)
      
      sec[i].addWidget(Buttonset4pickup);
    
    for(var k=0;k<d[i];k++){
      string ="drop$"+(i+1)+"@"+(k+1);
      name="drop "+(k+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
        var action4 = CardService.newAction().setFunctionName('adddrop').setParameters({"ind" : ""+(i+1)});
        var action5 = CardService.newAction().setFunctionName('removedrop').setParameters({"ind" : ""+(i+1)});
        var TextButton4= CardService.newTextButton().setText('+drop')
        .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action4);
      var TextButton42=CardService.newTextButton().setText('-drop')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action5);
      
        var Buttonset4drop=CardService.newButtonSet().addButton(TextButton4).addButton(TextButton42);
        
        sec[i].addWidget(Buttonset4drop);

      
        card.addSection(sec[i]).build();
    
    
    
  }
  
    var TextButton2= CardService.newTextButton().setText('place Order')
  .setBackgroundColor("#E54131").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
  .setOnClickAction(action1);
  
  var Buttonset =CardService.newButtonSet().addButton(TextButton2)
  section3.addWidget(Buttonset)
  
  card.addSection(section3).build();
  
  return CardService.newNavigation().updateCard(card.build());
}


function removedrop(e)
{
  var accessToken = e.messageMetadata.accessToken;
  GmailApp.setCurrentMessageAccessToken(accessToken);

  var messageId = e.messageMetadata.messageId;
  var message = GmailApp.getMessageById(messageId);
  var sender = message.getFrom();

  var email=sender.split("<")[1].split(">")[0];

  var body = message.getPlainBody();
  
  console.log(body);
  
  var parameter = e.parameters;
  var final = parameter["ind"];
  
    paramms = {"content" : body }
    var options = 
        {
          "method" : "POST",
          "contentType" : "application/json",
          "payload" :  JSON.stringify(paramms),
          "muteHttpExceptions" : true
          
        };
  
  var response = UrlFetchApp.fetch('https://instavans-gmailaddon.herokuapp.com/post',options);
  
  var data_main = JSON.parse(response);
  var data =data_main["main"];
  var date=data_main["date"];
  var mobile = data_main["mobile"]
  
  
  updated_data=e.formInput;
  console.log("pickup is ", e.formInput);
  var p = new Array(data.length);
  var d = new Array(data.length);
  var v = new Array(data.length);
  for(var i =0;i<data.length; i++)
  {
    p[i]=0;
    d[i]=0;
    v[i]=0;
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0]=="vehicle_type")
      {
        var temp =key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        
        if(max>v[temp-1])
        {
          v[temp-1]=max;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "pickup")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("max is " , typeof(max))
        if(max>p[temp-1])
        {
          p[temp-1]=max;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "drop")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("drop max is " , max)
        if(max>d[temp-1])
        {
          d[temp-1]=max;
        }
      }
    }
  }
  for(var i =0;i<data.length; i++)
  {
    console.log("p[i]",typeof(p[i])," d[i] ", d[i], "v[i] ",v[i]);
  }
  
   var card = CardService.newCardBuilder();
  

  
  var section = CardService.newCardSection().setHeader('<b><font color="#4285F4">PERSONAL DETAILS</font></b>')
  
  var section2 = CardService.newCardSection().setHeader('<b><font color="#4285F4">DROP ADDRESS</font></b>');
  
  var section3 = CardService.newCardSection();
  var action1 = CardService.newAction().setFunctionName('placeOrder');

  var action2 = CardService.newAction().setFunctionName('changeValue2');
  section.addWidget(CardService.newTextInput().setFieldName("username").setTitle("Username").setValue(message.getFrom())).setCollapsible(true);
  section.addWidget(CardService.newTextInput().setFieldName("emailId").setTitle("emailId").setValue(email)).setCollapsible(true);
  for(var mob = 0; mob<mobile.length; mob++)
  {
    var string = "mobile"+(mob+1);
    section.addWidget(CardService.newTextInput().setFieldName(string).setTitle("Mobile No.").setValue(mobile[mob])).setCollapsible(true);
  }
  section.addWidget(CardService.newTextInput().setFieldName("date").setTitle("Date").setValue(date[0]))
  card.addSection(section).build();
  //update right now
  
  var sec = new Array(data.length);

  
  for(var i=0;i<data.length;i++)
  {
    
    sec[i]= CardService.newCardSection().setHeader('<b><font color="#4285F4">ORDER </font></b>'+'<b><font color="#4285F4">'+(i+1)+ '</font></b>');
//    var string = "vehicle_type$"+(i+1);
//    sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle("Vehicle").setValue(data[i].vehicle_type));
    
    for(var x=0 ;x<v[i];x++)
    {
      var string = "vehicle_type$"+(i+1)+"@"+(x+1);
      var name = "vehicle "+(x+1);
      //enter here vevery thing related to vehicle
      var tf=[false,false,false,false,false,false,false,false,false]
      var veh_type=["tata ace","tata super ace","tata 407","canter 14","canter 17","canter 19","canter 20","bolero","dost"];
      var val = updated_data[string];
      for(var vt=0;vt<veh_type.length;vt++)
      {
        if(val==veh_type[vt])
        {
          tf[vt]=true;
        }
      }
//      var string = "vehicle_type$"+(i+1)+"@"+(v+1);
      var dropdown=CardService.newSelectionInput()
    .setType(CardService.SelectionInputType.DROPDOWN)
    .setTitle(name).setFieldName(string)
    .addItem("Tata Ace", "tata ace", tf[0])
    .addItem("Tata Super Ace", "tata super ace", tf[1])
      .addItem("tata 407", "tata 407", tf[2])
      .addItem("canter 14","canter 14", tf[3])
      .addItem("canter 17","canter 17", tf[4])
      .addItem("canter 19","canter 19", tf[5])
      .addItem("canter 20","canter 20", tf[6])
      .addItem("Bolero","bolero", tf[7])
      .addItem("Dost","dost", tf[8])
      
    sec[i].addWidget(dropdown);
      
    }
    
      var action7 = CardService.newAction().setFunctionName('addvehicle').setParameters({"ind":""+(i+1)});
      var action8= CardService.newAction().setFunctionName('removevehicle').setParameters({"ind":""+(i+1)});
      var TextButton7= CardService.newTextButton().setText('+vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action7);
      var TextButton8 =CardService.newTextButton().setText('-vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action8);
      
      var Buttonset4vehicle = CardService.newButtonSet().addButton(TextButton7).addButton(TextButton8)
      sec[i].addWidget(Buttonset4vehicle);
    
    for(var j=0;j<p[i];j++)
    {
      var string= "pickup$"+(i+1)+"@"+(j+1);
      var name ="pickup "+(j+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }

    
      var action3 = CardService.newAction().setFunctionName('addpickup').setParameters({"ind":""+(i+1)});
      var action6= CardService.newAction().setFunctionName('removepickup').setParameters({"ind":""+(i+1)});
      var TextButton3= CardService.newTextButton().setText('+PickUp')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action3);
      var TextButton32 =CardService.newTextButton().setText('-pickup')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action6);
      
      var Buttonset4pickup = CardService.newButtonSet().addButton(TextButton3).addButton(TextButton32)
      
      sec[i].addWidget(Buttonset4pickup);
      if((i+1)==final)
  {
    d[i]=d[i]-1;
  }
    for(var k=0;k<d[i];k++){
      string ="drop$"+(i+1)+"@"+(k+1);
      name="drop "+(k+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
    
        var action4 = CardService.newAction().setFunctionName('adddrop').setParameters({"ind" : ""+(i+1)});
        var action5 = CardService.newAction().setFunctionName('removedrop').setParameters({"ind" : ""+(i+1)});
        var TextButton4= CardService.newTextButton().setText('+drop')
        .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action4);
      var TextButton42=CardService.newTextButton().setText('-drop')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action5);
      
        var Buttonset4drop=CardService.newButtonSet().addButton(TextButton4).addButton(TextButton42);
        
        sec[i].addWidget(Buttonset4drop);

      
        card.addSection(sec[i]).build();
    
    
    
  }
  
    var TextButton2= CardService.newTextButton().setText('place Order')
  .setBackgroundColor("#E54131").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
  .setOnClickAction(action1);
  
  var Buttonset =CardService.newButtonSet().addButton(TextButton2)
  section3.addWidget(Buttonset)
  
  card.addSection(section3).build();
  
  return CardService.newNavigation().updateCard(card.build());
  
}

function addvehicle(e)
{
  var accessToken = e.messageMetadata.accessToken;
  GmailApp.setCurrentMessageAccessToken(accessToken);

  var messageId = e.messageMetadata.messageId;
  var message = GmailApp.getMessageById(messageId);
  var sender = message.getFrom();

  var email=sender.split("<")[1].split(">")[0];

  var body = message.getPlainBody();
  
  console.log(body);
  
  var parameter = e.parameters;
  var final = parameter["ind"];
  
    paramms = {"content" : body }
    var options = 
        {
          "method" : "POST",
          "contentType" : "application/json",
          "payload" :  JSON.stringify(paramms),
          "muteHttpExceptions" : true
          
        };
  
  var response = UrlFetchApp.fetch('https://instavans-gmailaddon.herokuapp.com/post',options);
  var data_main = JSON.parse(response);
  var data =data_main["main"];
  var date=data_main["date"];
  var mobile = data_main["mobile"]
  
  
  updated_data=e.formInput;
  console.log("pickup is ", e.formInput);
  var p = new Array(data.length);
  var d = new Array(data.length);
  var v = new Array(data.length);
  for(var i =0;i<data.length; i++)
  {
    p[i]=0;
    d[i]=0;
    v[i]=0;
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0]=="vehicle_type")
      {
        var temp =key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        
        if(max>v[temp-1])
        {
          v[temp-1]=max;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "pickup")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("max is " , typeof(max))
        if(max>p[temp-1])
        {
          p[temp-1]=max;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "drop")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("drop max is " , max)
        if(max>d[temp-1])
        {
          d[temp-1]=max;
        }
      }
    }
  }
  for(var i =0;i<data.length; i++)
  {
    console.log("p[i]",typeof(p[i])," d[i] ", d[i], "v[i] ",v[i]);
  }
  
   var card = CardService.newCardBuilder();
  

  
  var section = CardService.newCardSection().setHeader('<b><font color="#4285F4">PERSONAL DETAILS</font></b>')
  
  var section2 = CardService.newCardSection().setHeader('<b><font color="#4285F4">DROP ADDRESS</font></b>');
  
  var section3 = CardService.newCardSection();
  var action1 = CardService.newAction().setFunctionName('placeOrder');

  var action2 = CardService.newAction().setFunctionName('changeValue2');
  section.addWidget(CardService.newTextInput().setFieldName("username").setTitle("Username").setValue(message.getFrom())).setCollapsible(true);
  section.addWidget(CardService.newTextInput().setFieldName("emailId").setTitle("emailId").setValue(email)).setCollapsible(true);
  for(var mob = 0; mob<mobile.length; mob++)
  {
    var string = "mobile"+(mob+1);
    section.addWidget(CardService.newTextInput().setFieldName(string).setTitle("Mobile No.").setValue(mobile[mob])).setCollapsible(true);
  }
  section.addWidget(CardService.newTextInput().setFieldName("date").setTitle("Date").setValue(date[0]))
  card.addSection(section).build();
  //update right now
  
  var sec = new Array(data.length);

  
  for(var i=0;i<data.length;i++)
  {
    
    sec[i]= CardService.newCardSection().setHeader('<b><font color="#4285F4">ORDER </font></b>'+'<b><font color="#4285F4">'+(i+1)+ '</font></b>');
//    var string = "vehicle_type$"+(i+1);
//    sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle("Vehicle").setValue(data[i].vehicle_type));
    
    for(var x=0 ;x<v[i];x++)
    {
      var string = "vehicle_type$"+(i+1)+"@"+(x+1);
      var name = "vehicle "+(x+1);
      //enter here vevery thing related to vehicle
      var tf=[false,false,false,false,false,false,false,false,false]
      var veh_type=["tata ace","tata super ace","tata 407","canter 14","canter 17","canter 19","canter 20","bolero","dost"];
      var val = updated_data[string];
      for(var vt=0;vt<veh_type.length;vt++)
      {
        if(val==veh_type[vt])
        {
          tf[vt]=true;
        }
      }
//      var string = "vehicle_type$"+(i+1)+"@"+(v+1);
      var dropdown=CardService.newSelectionInput()
    .setType(CardService.SelectionInputType.DROPDOWN)
    .setTitle(name).setFieldName(string)
    .addItem("Tata Ace", "tata ace", tf[0])
    .addItem("Tata Super Ace", "tata super ace", tf[1])
      .addItem("tata 407", "tata 407", tf[2])
      .addItem("canter 14","canter 14", tf[3])
      .addItem("canter 17","canter 17", tf[4])
      .addItem("canter 19","canter 19", tf[5])
      .addItem("canter 20","canter 20", tf[6])
      .addItem("Bolero","bolero", tf[7])
      .addItem("Dost","dost", tf[8])
      
    sec[i].addWidget(dropdown);
      
    }
      if((i+1)==final)
  {
    string = "vehicle_type$"+(i+1)+"@"+(v[i]+1);
    name="vehicle "+(v[i]+1);
     var dropdown=CardService.newSelectionInput()
    .setType(CardService.SelectionInputType.DROPDOWN)
    .setTitle(name).setFieldName(string)
    .addItem("Tata Ace", "tata ace", true)
    .addItem("Tata Super Ace", "tata super ace", false)
      .addItem("tata 407", "tata 407", false)
      .addItem("canter 14","canter 14", false)
      .addItem("canter 17","canter 17", false)
      .addItem("canter 19","canter 19", false)
      .addItem("canter 20","canter 20", false)
      .addItem("Bolero","bolero", false)
      .addItem("Dost","dost", false)
      
    sec[i].addWidget(dropdown);
    
  }
    
      var action7 = CardService.newAction().setFunctionName('addvehicle').setParameters({"ind":""+(i+1)});
      var action8= CardService.newAction().setFunctionName('removevehicle').setParameters({"ind":""+(i+1)});
      var TextButton7= CardService.newTextButton().setText('+vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action7);
      var TextButton8 =CardService.newTextButton().setText('-vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action8);
      
      var Buttonset4vehicle = CardService.newButtonSet().addButton(TextButton7).addButton(TextButton8)
      sec[i].addWidget(Buttonset4vehicle);
    
    for(var j=0;j<p[i];j++)
    {
      var string= "pickup$"+(i+1)+"@"+(j+1);
      var name ="pickup "+(j+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
  
    
      var action3 = CardService.newAction().setFunctionName('addpickup').setParameters({"ind":""+(i+1)});
      var action6= CardService.newAction().setFunctionName('removepickup').setParameters({"ind":""+(i+1)});
      var TextButton3= CardService.newTextButton().setText('+PickUp')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action3);
      var TextButton32 =CardService.newTextButton().setText('-pickup')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action6);
      
      var Buttonset4pickup = CardService.newButtonSet().addButton(TextButton3).addButton(TextButton32)
      
      sec[i].addWidget(Buttonset4pickup);
    
    for(var k=0;k<d[i];k++){
      string ="drop$"+(i+1)+"@"+(k+1);
      name="drop "+(k+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
        var action4 = CardService.newAction().setFunctionName('adddrop').setParameters({"ind" : ""+(i+1)});
        var action5 = CardService.newAction().setFunctionName('removedrop').setParameters({"ind" : ""+(i+1)});
        var TextButton4= CardService.newTextButton().setText('+drop')
        .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action4);
      var TextButton42=CardService.newTextButton().setText('-drop')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action5);
      
        var Buttonset4drop=CardService.newButtonSet().addButton(TextButton4).addButton(TextButton42);
        
        sec[i].addWidget(Buttonset4drop);

      
        card.addSection(sec[i]).build();
    
    
    
  }
  
    var TextButton2= CardService.newTextButton().setText('place Order')
  .setBackgroundColor("#E54131").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
  .setOnClickAction(action1);
  
  var Buttonset =CardService.newButtonSet().addButton(TextButton2)
  section3.addWidget(Buttonset)
  
  card.addSection(section3).build();
  
  return CardService.newNavigation().updateCard(card.build());
}
function removevehicle(e)
{
  var accessToken = e.messageMetadata.accessToken;
  GmailApp.setCurrentMessageAccessToken(accessToken);

  var messageId = e.messageMetadata.messageId;
  var message = GmailApp.getMessageById(messageId);
  var sender = message.getFrom();

  var email=sender.split("<")[1].split(">")[0];

  var body = message.getPlainBody();
  
  console.log(body);
  
  var parameter = e.parameters;
  var final = parameter["ind"];
  
    paramms = {"content" : body }
    var options = 
        {
          "method" : "POST",
          "contentType" : "application/json",
          "payload" :  JSON.stringify(paramms),
          "muteHttpExceptions" : true
          
        };
  
  var response = UrlFetchApp.fetch('https://instavans-gmailaddon.herokuapp.com/post',options);
  var data_main = JSON.parse(response);
  var data =data_main["main"];
  var date=data_main["date"];
  var mobile = data_main["mobile"]
  
  
  updated_data=e.formInput;
  console.log("pickup is ", e.formInput);
  var p = new Array(data.length);
  var d = new Array(data.length);
  var v = new Array(data.length);
  for(var i =0;i<data.length; i++)
  {
    p[i]=0;
    d[i]=0;
    v[i]=0;
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0]=="vehicle_type")
      {
        var temp =key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        
        if(max>v[temp-1])
        {
          v[temp-1]=max;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "pickup")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("max is " , typeof(max))
        if(max>p[temp-1])
        {
          p[temp-1]=max;
        }
      }
    }
  }
  for(var key in updated_data)
  {
    if(updated_data.hasOwnProperty(key))
    {
      if(key.split('$')[0] == "drop")
      {
        var temp = key.split('$')[1].split('@')[0];
        var max = key.split('@')[1];
        max=parseInt(max);
        temp=parseInt(temp);
        console.log("drop max is " , max)
        if(max>d[temp-1])
        {
          d[temp-1]=max;
        }
      }
    }
  }
  for(var i =0;i<data.length; i++)
  {
    console.log("p[i]",typeof(p[i])," d[i] ", d[i], "v[i] ",v[i]);
  }
  
   var card = CardService.newCardBuilder();
  

  
  var section = CardService.newCardSection().setHeader('<b><font color="#4285F4">PERSONAL DETAILS</font></b>')
  
  var section2 = CardService.newCardSection().setHeader('<b><font color="#4285F4">DROP ADDRESS</font></b>');
  
  var section3 = CardService.newCardSection();
  var action1 = CardService.newAction().setFunctionName('placeOrder');

  var action2 = CardService.newAction().setFunctionName('changeValue2');
  section.addWidget(CardService.newTextInput().setFieldName("username").setTitle("Username").setValue(message.getFrom())).setCollapsible(true);
  section.addWidget(CardService.newTextInput().setFieldName("emailId").setTitle("emailId").setValue(email)).setCollapsible(true);
  for(var mob = 0; mob<mobile.length; mob++)
  {
    var string = "mobile"+(mob+1);
    section.addWidget(CardService.newTextInput().setFieldName(string).setTitle("Mobile No.").setValue(mobile[mob])).setCollapsible(true);
  }
  section.addWidget(CardService.newTextInput().setFieldName("date").setTitle("Date").setValue(date[0]))
  card.addSection(section).build();
  //update right now
  
  var sec = new Array(data.length);

  
  for(var i=0;i<data.length;i++)
  {
    
    sec[i]= CardService.newCardSection().setHeader('<b><font color="#4285F4">ORDER </font></b>'+'<b><font color="#4285F4">'+(i+1)+ '</font></b>');
//    var string = "vehicle_type$"+(i+1);
//    sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle("Vehicle").setValue(data[i].vehicle_type));
       if((i+1)==final)
  {
    v[i]=v[i]-1;
    
  }
    for(var x=0 ;x<v[i];x++)
    {
      var string = "vehicle_type$"+(i+1)+"@"+(x+1);
      var name = "vehicle "+(x+1);
      //enter here vevery thing related to vehicle
      var tf=[false,false,false,false,false,false,false,false,false]
      var veh_type=["tata ace","tata super ace","tata 407","canter 14","canter 17","canter 19","canter 20","bolero","dost"];
      var val = updated_data[string];
      for(var vt=0;vt<veh_type.length;vt++)
      {
        if(val==veh_type[vt])
        {
          tf[vt]=true;
        }
      }
//      var string = "vehicle_type$"+(i+1)+"@"+(v+1);
      var dropdown=CardService.newSelectionInput()
    .setType(CardService.SelectionInputType.DROPDOWN)
    .setTitle(name).setFieldName(string)
    .addItem("Tata Ace", "tata ace", tf[0])
    .addItem("Tata Super Ace", "tata super ace", tf[1])
      .addItem("tata 407", "tata 407", tf[2])
      .addItem("canter 14","canter 14", tf[3])
      .addItem("canter 17","canter 17", tf[4])
      .addItem("canter 19","canter 19", tf[5])
      .addItem("canter 20","canter 20", tf[6])
      .addItem("Bolero","bolero", tf[7])
      .addItem("Dost","dost", tf[8])
      
    sec[i].addWidget(dropdown);
      
    }
   
    
      var action7 = CardService.newAction().setFunctionName('addvehicle').setParameters({"ind":""+(i+1)});
      var action8= CardService.newAction().setFunctionName('removevehicle').setParameters({"ind":""+(i+1)});
      var TextButton7= CardService.newTextButton().setText('+vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action7);
      var TextButton8 =CardService.newTextButton().setText('-vehicle')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action8);
      
      var Buttonset4vehicle = CardService.newButtonSet().addButton(TextButton7).addButton(TextButton8)
      sec[i].addWidget(Buttonset4vehicle);
    
    for(var j=0;j<p[i];j++)
    {
      var string= "pickup$"+(i+1)+"@"+(j+1);
      var name ="pickup "+(j+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
  
    
      var action3 = CardService.newAction().setFunctionName('addpickup').setParameters({"ind":""+(i+1)});
      var action6= CardService.newAction().setFunctionName('removepickup').setParameters({"ind":""+(i+1)});
      var TextButton3= CardService.newTextButton().setText('+PickUp')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action3);
      var TextButton32 =CardService.newTextButton().setText('-pickup')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
      .setOnClickAction(action6);
      
      var Buttonset4pickup = CardService.newButtonSet().addButton(TextButton3).addButton(TextButton32)
      
      sec[i].addWidget(Buttonset4pickup);
    
    for(var k=0;k<d[i];k++){
      string ="drop$"+(i+1)+"@"+(k+1);
      name="drop "+(k+1);
      sec[i].addWidget(CardService.newTextInput().setFieldName(string).setTitle(name).setMultiline(true).setValue(updated_data[string]));
    }
        var action4 = CardService.newAction().setFunctionName('adddrop').setParameters({"ind" : ""+(i+1)});
        var action5 = CardService.newAction().setFunctionName('removedrop').setParameters({"ind" : ""+(i+1)});
        var TextButton4= CardService.newTextButton().setText('+drop')
        .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action4);
      var TextButton42=CardService.newTextButton().setText('-drop')
      .setBackgroundColor("#4285F4").setTextButtonStyle(CardService.TextButtonStyle.FILLED).setOnClickAction(action5);
      
        var Buttonset4drop=CardService.newButtonSet().addButton(TextButton4).addButton(TextButton42);
        
        sec[i].addWidget(Buttonset4drop);

      
        card.addSection(sec[i]).build();
    
    
    
  }
  
    var TextButton2= CardService.newTextButton().setText('place Order')
  .setBackgroundColor("#E54131").setTextButtonStyle(CardService.TextButtonStyle.FILLED)
  .setOnClickAction(action1);
  
  var Buttonset =CardService.newButtonSet().addButton(TextButton2)
  section3.addWidget(Buttonset)
  
  card.addSection(section3).build();
  
  return CardService.newNavigation().updateCard(card.build());
}

//place order
//this will check for validation :
//if all columns are properly filled then it will show place the order else it will show error
function placeOrder(e)
{
  
  
  
  var fetch = JSON.stringify(e.formInput);
  var data=JSON.parse(fetch);
  console.log("data in place order is", data);
  var substr="$";
  for (var key in data) 
  {
    if (data.hasOwnProperty(key))
    {
      if(data[key]==""|| data[key]==" " || data[key]=="  " || data[key]==null)
      {
        if(data[key].indexOf(substr)==-1)
        {
          var element = key;
          return CardService.newActionResponseBuilder()
      .setNotification(CardService.newNotification()
          .setText("please fill or remove "+element))
      .build();
        }
        else
        {
        var order = key.split('$')[1].split('@')[0];
        var element = key.split('$')[0];
        var number = "";
        number=key.split('@')[1];
        
        return CardService.newActionResponseBuilder()
      .setNotification(CardService.newNotification()
          .setText("please fill or remove "+element + " "+number +" of order "+order))
      .build();
        }
      }
//      else
//      {
//        var card = CardService.newCardBuilder();
//        var section = CardService.newCardSection().setHeader('<b><font color="#006600">ORDER PLACED!</font></b>')
//        return card.addSection(section).build();
//          
//      }
    }
  }
}


//  var response = UrlFetchApp.fetch('http://www.mocky.io/v2/5d09db463400003728d8302e');
