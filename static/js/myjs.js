Webcam.set({
    width:320,
    height:240,
    image_type:'jpeg',
    jpeg_quality:90
});
Webcam.attach("#my_camera");
function take_snapshot(){
    Webcam.snap(function(data_uri){
        document.getElementById('result').innerHTML="<img id='imageprev' src='"+data_uri+"'>";
        document.getElementById('myidno').innerHTML=document.getElementById('idno').value;
        document.getElementById('mylastname').innerHTML=document.getElementById('lastname').value;
        document.getElementById('myfirstname').innerHTML=document.getElementById('firstname').value;
        document.getElementById('mycourse').innerHTML=document.getElementById('course').value;
        document.getElementById('mylevel').innerHTML=document.getElementById('level').value;
    });
}
function save_snapshot(){
    var base64image=document.getElementById('imageprev').src;
    var idno=document.getElementById('idno').value;
    var lastname=document.getElementById('lastname').value;
    var firstname=document.getElementById('firstname').value;
    var course=document.getElementById('course').value;
    var level=document.getElementById('level').value;

    Webcam.upload(base64image,"upload?idno="+idno+"&lastname="+lastname+"&firstname="+firstname+"&course="+course+"&level="+level,function(code,name){
        alert("image uploaded...");

        document.getElementById('idno').value='';
        document.getElementById('lastname').value='';
        document.getElementById('firstname').value='';
        document.getElementById('course').value='';
        document.getElementById('level').value='';
        document.getElementById('idno').focus();
        //Webcam.reset();
    });

}
