// Array methods
// map()
let numbers = [1,2,3,4];
let result = numbers.map(num => num * 2);
console.log(result);
// Output: [2, 4, 6, 8]

// filter()
let numbers = [1,2,3,4,5,6];
let even = numbers.filter(num => num % 2 === 0);
console.log(even);
// [ 2, 4, 6 ]

// reduce()
let numbers = [1,2,3,4,5]
let sum = numbers.reduce((total, num) => total + num, 0);
console.log(sum);
// output: 10

// find()
let numbers = [5, 10, 15, 20];
let result = numbers.find(num => num > 10);
console.log(result);
// output: 15

// forEach()
let fruits = ["Apple", "banana", "mango"];
fruits.forEach(fruit => {
    console.log(fruit);
});
// Apple
// Banana
// Mango

// some()
// Returns true if at least one element matches the condition.
let numbers = [1, 3, 5, 8];
let hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven);
// Output: true

// every()
let numbers = [2, 4, 6, 8];
let allEven = numbers.every(num => num % 2 === 0);
console.log(allEven);
// Output: true


<!DOCTYPE html>
<html>
<head>
    <title>DOM Example</title>
</head>
<body>
<h1 id="title">Hello World</h1>
<button id="btn">Click Me</button>
<script>
    const button = document.getElementById("btn");
    button.addEventListener("click", function () {
        document.getElementById("title").textContent = "Button Clicked!";
    });
</script>
</body>
</html>


// This Keyword and Arrow Function
// Arrow Function 
const add = (a, b) => a + b;
console.log(add(5,3));
// 8

const person = {
  name: "Ankit",
  normalFunction: function () {
    console.log("Normal:", this.name);
  },
  arrowFunction: () => {
    console.log("Arrow:", this.name);
  }
};
person.normalFunction();
person.arrowFunction();
// Normal: Ankit
// Arrow: undefined


const arr = [1, 2];
const newArr = [...arr, 3];
console.log(newArr);

// Temporal Dead Zone (TDZ) 
console.log(a);
let a = 10;
// Output : ReferenceError


// modules
// math.js
export function add(a,b){
    return a+b;
}
// app.js
import {add} from "./math.js";
console.log(add(5,3));


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

