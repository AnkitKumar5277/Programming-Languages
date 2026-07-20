// var, let, and const
// var
var a = 10;
console.log(a);
var a = 20;
a = 30;
console.log(a);
// 10
// 30

// let
let b = 20;
console.log(b);
// let b = 30; // -> failed cannot redeclare
b = 40;
console.log(b);
// 20
// 40

// const
const c = 30;
console.log(c); // 30
// const c = 40; // ❌ Error: Cannot redeclare
// c = 50;        // ❌ Error: Cannot reassign


// == aur === difference
// == loose equality
let a = 5;
let b = "5";
console.log(a == b);
// true

// === strict equality
let a = 5;
let b = "5";
console.log(a ===b);
// false


// Hoisting
console.log(a)
var a = 10;
console.log(a)
// undefined
// 10

var a;            // Hoisted
console.log(a);   // undefined
a = 10;
console.log(a);   // 10
// undefined
// 10


// Global Scope
let name = "ankit"; // Global variable
function showname() {
  console.log(name) 
}
showname();
console.log(name);
// ankit
// ankit


// Function Scope
function demo() {
    var age = 22;
    console.log(age);
}
demo();
// console.log(age); -> Error
// 22


// Block Scope
if (true) {
    let city = "Delhi";
    const country = "India";
    console.log(city);
    console.log(country);
}
// Delhi
// India
// console.log(city);      // Error
// console.log(country);   // Error


