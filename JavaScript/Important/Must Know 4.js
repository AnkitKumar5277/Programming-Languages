// template literals
let name = "Ankit";
let age = 22;
let message = `My name is ${name} and I am ${age} years old.`;
console.log(message);


// nan
console.log(0 / 0);        // NaN
console.log(Number("abc")); // NaN
console.log(Math.sqrt(-1)); // NaN

// Synchronous
console.log("Start");
function add() {
  console.log(10 + 20);
}
add();
console.log("End");
// Start
// 30
// End

// Asynchronous (Non-Blocking)
console.log("Start");
setTimeout(() => {
  console.log("Task Completed");
}, 2000);
console.log("End");
// Start
// End
// Task Completed


// setTimeout()
console.log("Start");
setTimeout(() => {
  console.log("Task Completed");
}, 2000);
console.log("End");
// Start
// End
// Task Completed

// setInterval() Example
let id = setInterval(() => {
  console.log("Hello");
}, 2000);
// (After 2 sec)
// Hello
// (After 2 sec)
// Hello
// (After 2 sec)
// Hello
// ...


// slice() Example (Original array safe)
let fruits = ["Apple", "Banana", "Mango", "Orange"];
let result = fruits.slice(1, 3);
console.log(result);
console.log(fruits);
// ["Banana", "Mango"]
// ["Apple", "Banana", "Mango", "Orange"]

// 2. splice() Example (Remove Elements)
let fruits = ["Apple", "Banana", "Mango", "Orange"];
let removed = fruits.splice(1, 2);
console.log(removed);
console.log(fruits);
// Output
// ["Banana", "Mango"]
// ["Apple", "Orange"]


// Array
let fruits = ["Apple", "Banana", "Mango"];
console.log(fruits);
console.log(fruits[0]); // Apple
console.log(fruits[1]); // Banana
console.log(fruits[2]); // Mango

// objects
let student = {
    name: "Ankit",
    age: 22,
    city: "Delhi"
};
console.log(student);
console.log(student.name);
console.log(student.age);
console.log(student.city);
