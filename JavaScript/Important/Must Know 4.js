let name = "Ankit";
let age = 22;
let message = `My name is ${name} and I am ${age} years old.`;
console.log(message);


// nan
console.log(0 / 0);        // NaN
console.log(Number("abc")); // NaN
console.log(Math.sqrt(-1)); // NaN



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

