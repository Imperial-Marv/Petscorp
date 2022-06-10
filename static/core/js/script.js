


var lista =[]
function agregarTabla() {
    var usuario = {
        "user":"",
        "pass":"",
        "direc":"",
        "mail":"",
    }

    var user = document.getElementById("user").value;
    usuario.user=user;
    console.log(usuario);

    var desc = document.getElementById("pass").value;
    usuario.pass=pass;
    console.log(pass);

    var pass = document.getElementById("direc").value;
    usuario.direc=direc;
    console.log(direc);

    var type = document.getElementById("mail").value;
    usuario.mail=mail
    console.log(mail)

    var table = document.getElementById("bodyTabla1");
    var tab = document.getElementById("tabla1").rows.length; 
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    cell1.innerHTML = user;
    cell2.innerHTML = pass;
    cell3.innerHTML = direc;
    cell4.innerHTML = email;
    cell5.innerHTML = '<button type="button" class="btn btn-danger" onclick="deleteRow(this)">Eliminar</button>';
    if(tab>0){
        document.getElementById("tabla1").style.visibility="visible";
    }
    lista.push(usuario)
}

function deleteRow(r) {
    var i = r.parentNode.parentNode.rowIndex;
    document.getElementById("tabla1").deleteRow(i);
    
    var tab = document.getElementById("bodyTabla1").rows.length; 
    if(tab<=0){
        document.getElementById("tabla1").style.visibility="hidden";
    }
}  