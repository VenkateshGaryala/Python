function printerror(eleid,hintmsg){
document.getElementById(eleid).innnerHTML=hintmsg;
}
function validateForm(){
var name=document.contactform.name.value;
var email=document.contactform.email.value;
var mobile=document.contactform.mobile.value;
var country=document.contactform.country.value;
var gender=document.contactform.gender.value;
var hobbies=[];
var checkboxes=document.getElementsByName("hobbies[]");
for(var i=0;i<checkboxes.length;i++){
if(checkboxes[i].checked){
hobbies.push(checkboxes[i].value);
}
}
var nameerr=emailerr=mobileerr=countryerr=gendererr=true;
if(name==""){
printerror("nameerr","please enter your name");
}else{
var regex=/^[a-zA-Z\s]+$/;
if(regex.test(name)===false){
printerror("nameerr","please enter a valid name");
}
else{
printerror("nameerr","");
nameerr=false;
}
}
if(email==""){
printerror("emailerr","please enter your email");
}
else{
var regex=/^\S+@\S+\.\S+$/;
if(regex.test(email)===false){
printerror("emailerr",please enter valid email");
}
else{
printerror("emailerr","");
emailerr=false;
}
}
if(mobile==""){
printerror("mobileerr","please enter your email");
}
else{
var regex=/^[1-9]\d[9]$/;
if(regex.test(mobile)===false){
printerror("mobileerr",please enter valid email");
}
else{
printerror("mobileerr","");
mobileerr=false;
}
}
if(country=="Select"){
printerror("countryerr","please enter your email");
}
else{
printerror("countryerr","");
countryerr=false;
}
if(gender==""){
printerror("gendererr","please enter your email");
}
else{
printerror("gendererr","");
gendererr=false;
}
if((nameerr||emailerr||mobileerr||countryerr||gendererr)==true){
return false;
}
else{
var datapre="you have entered the following details:+"full name:"+name+"email"+email+"mobile"+mobile+"country"+country+"gender"+gender;
if(hobbies.length){
datapre+="hobbies"+hobbies.join(",");
}
alert(datapre);
}
};