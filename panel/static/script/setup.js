function addOps(path, ops) {
    axios.get(path + ops.name + "/" + ops.value).then(

    );
}

document.getElementById("submitButton").onclick = function() {
    const tokenField = document.getElementById("tokenField").value;
    const nameField = document.getElementById("nameField").value;
    const serverKeyField = document.getElementById("serverKeyField").value;
    queryToken = {"name":"token", "value":tokenField};
    queryName = {"name":"name", "value":nameField};
    queryServerKey = {"name":"serverKey", "value":serverKeyField};
    querySetup = {"name":"setup", "value":"true"};
    addOps('http://localhost:8000/addoption/', queryToken);
    addOps('http://localhost:8000/addoption/', queryName);
    addOps('http://localhost:8000/addoption/', queryServerKey);
    addOps('http://localhost:8000/changeoption/', querySetup);
    window.location.reload();
}