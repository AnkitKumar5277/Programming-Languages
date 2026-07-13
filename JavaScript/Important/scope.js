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

