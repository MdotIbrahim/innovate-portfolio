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

//! STRING INTERPOLATION

console.log(`Your name is ${myFirstName} ${mySurname}.`)

//! ARRAYS

let innovateInstructors = ["Jordan", "Katy"];

console.log(innovateInstructors);
console.log(innovateInstructors[1]);

//! LOOPS

let text = ""

for (let i = 0; i < 5; i++) {
    text += "the number is " + i + " ";
}console.log(text)

let i = 5
while (i < 10) {
    text = text += "the number is " + i;
    i++;
}console.log(text)

//! SWITCH STATEMENTS
let fruit = "apple";
switch (fruit) {
    case "grape":
        console.log("grape");
        break;
    case "orange":
        console.log("orange");
        break;
    case "apple":
        console.log("apple!");
        break;
    default:
        console.log("I don't like that fruit.")
}

//! ARROW FUNCTIONS

hello = () => {
    console.log("Hello World!");
}

hello()