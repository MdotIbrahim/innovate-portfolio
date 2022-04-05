function darkMode() {
    let page = document.body; //this is the body of html
    page.classList.toggle("dark-mode"); //execute and reverse command with toggle.
}

function mOver() {
    document.getElementById("title").style.color = "khaki";
} 

function mOut() {
    document.getElementById("title").style.color =  "red";
}

$(document).ready(function() {
    $("#change-colour").click(function(){
        $("h2").toggleClass("pink-colour"); 
    });
});
