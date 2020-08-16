const NAVBAR_WIDTH = 80;

function onMenuButtonClick(){
    var navbar = document.getElementById("liskeNavbar");
    var menuButton = document.getElementById("menuButton");
    var hide = navbar.style.left == "-81%" || navbar.style.left == "" ? false : true;

    // Hide navbar on the left
    if(hide){
        var pos = 0
        var id = setInterval(frame, 3);
        function frame(){
            if(pos > NAVBAR_WIDTH){
                clearInterval(id)
            }else{
                pos++;
                navbar.style.left =  "-" + pos + "%";
            }
        }
    }else{
        var pos = 80
        var id = setInterval(frame, 3);
        function frame(){
            if(pos > NAVBAR_WIDTH){
                clearInterval(id)
            }else{
                pos--;
                navbar.style.left =  "-" + pos + "%";
            }
        }
    }

    //Switch the button text
    menuButton.innerText = hide ? ">" : "X";
}

function onNavButtonClick(clickedButton){
    var currenId = clickedButton.dataset["id"];

    if(!isNaN(currenId)){
        window.location.replace("http://127.0.0.1:5000/liske/" + currenId);
    }
}

function removeCurrentItem(clickedButton){
    var currenId = clickedButton.dataset["id"];
    var url = "http://127.0.0.1:5000/removetask/" + currenId;

    var config = {
        method: "DELETE"
    };

    fetch(url, config)
    .then(function(response){
        var activeLiskeId = document.getElementsByClassName("liske-active")[0].id;
        window.location.href = "http://127.0.0.1:5000/liske/" + activeLiskeId;
    })
    .catch(function(error){
        debugger;
    })
}

function showAddTaskForm(modalId){
    var courtine = document.getElementById("modalCourtine");
    var addTaskModal = document.getElementById(modalId);

    courtine.style.display = "block";
    addTaskModal.style.display = "flex";
}

function hideAddTaskForm(modalId){
    var courtine = document.getElementById("modalCourtine");
    var addTaskModal = document.getElementById(modalId);

    courtine.style.display = "none";
    addTaskModal.style.display = "none";
}