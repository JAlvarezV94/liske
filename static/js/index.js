const NAVBAR_WIDTH = 80;

function onMenuButtonClick(){
    var navbar = document.getElementById("liskeNavbar");
    var menuButton = document.getElementById("menuButton");
    var hide = navbar.style.left == "-81%" ? false : true;

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