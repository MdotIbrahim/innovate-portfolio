$(document).ready(function() {
    $("#change-colour").click(function(){
        $("h1").toggleClass("red-title"); // can put class or id to target specific
    });
    $("#hide-text").click(function(){
        $("p").toggle(); // hide() would only hide and not bring back
    });
    $("#dark-mode").click(function(){
        $("body").toggleClass("dark-mode");
    });
    
});


// console.log("Hello World")


// function displayDate(id) {
//     document.getElementById("date").innerHTML = Date();
// }
