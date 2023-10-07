function showMenu() {

    var mobileMenu = document.querySelector(".mobile-menu");
    var top_bar =document.querySelector("#top-bar");
    var middle_bar = document.querySelector("#middle-bar");
    var lower_bar = document.querySelector("#lower-bar");
   
    var  hiddenMenu = document.querySelector("#hidden");

    if(mobileMenu.dataset.menu == "on") {

       
        middle_bar.style.display = "none";
        top_bar.style.background="red";
        lower_bar.style.background="red";
        lower_bar.style.transform = "rotate(45deg) translate(-4px)";
        top_bar.style.transform = "rotate(-45deg) translate(-4px)";
        mobileMenu.dataset.menu = "off";
        hiddenMenu.style.display="block";
    }
   else {
    hiddenMenu.style.display = "none";
    top_bar.style.transform = "translate(4px) rotate(180deg) translate(4px) ";
    top_bar.style.background="white";
    lower_bar.style.background="white";
    lower_bar.style.transform = "translate(4px) rotate(-180deg) translate(4px) ";
    middle_bar.style.display ="block";
    mobileMenu.dataset.menu = "on";
   }
   
   


} 