// Object Destructuring
// Destructuring
const user = {
  name: "Ankit", 
  age: 22
};
const { name, age} = user;
console.log(name); // Ankit
console.log(age); // 22

// Array Destructuring
// Normal Way
let colors = ["Red", "Green", "Blue"];
let first = colors[0];
let second = colors[1];
console.log(first);   // Red
console.log(second);  // Green

// Using Destructuring
let colors = ["Red", "Green", "Blue"];
let [first, second] = colors;
console.log(first);   // Red
console.log(second);  // Green

