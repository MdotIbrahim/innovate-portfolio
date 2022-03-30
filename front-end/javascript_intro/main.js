// camelCase used in js
/* multi
line comment*/

console.log("Hello World");

//! DATA TYPES

let dataType = "this is a string"; // string data type

dataType = 1234; // integer data type

dataType = 123.456 // float data type

dataType = true // boolean data type. lower case.

//! VARIABLES
var myFirstName = "John"; // 'var' is used for ;egacy code

const mySurname = "Smith"; // 'const' cannot be updated

let myJob = "Not Free"; // 'let' can

myJob = "Free"

console.log(myJob)

//! IF STATEMENTS

if (myJob === "Not Free") {
    console.log("John is not free.");
} else if (myJob === "Free") {
    console.log("John is free.");
}else {
    console.log ("John has ascended.");
}

if (myFirstName === "John" && mySurname === "Smith") {
    console.log("John Smith is here.");
}else {
    console.log ("Who are you?");
}

if (myJob === "Free" || myJob === "Not Free") {
    console.log("John is here.");
}else {
    console.log ("John is gone.");
}

//! Functions

function myFunction() {
    console.log("This is a Javascript function")
}

myFunction()