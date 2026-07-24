// Data Types 
let num = 10;         // number
let bool = true;      // boolean
let arr = [1,2,3];    // array
let obj = {a:1};      // object

// Promise
let promise = new Promise((resolve, reject) => {
  console.log("Pending...");
  setTimeout(() => {
    let paymentSuccess = true;

    if (paymentSuccess) {
      resolve("Payment Successful");
    } else {
      reject("Payment Failed");
    }
  }, 3000);

});
promise
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.log(error);
  });
  
// Pending...
// Payment Successful

// if paymentSuccess = false):
// Payment Failed

// Async Await
// .then() aur .catch() ki jagah normal synchronous jaisa code likh sakte hain.
function getData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data received!");
    }, 2000);
  });
}
async function fetchData() {
  console.log("Fetching data...");
  let result = await getData();
  console.log(result);
}
fetchData();


// Event Loop
// setTimeout()
console.log("Start");
setTimeout(() => {
    console.log("Hello");
}, 2000);
console.log("End");
// Start
// End
// Hello - prints after 2 seconds

// Promise (Microtask Queue)

// Example 2: Promise (Microtask Queue)
console.log("Start");
Promise.resolve().then(() => {
    console.log("Promise");
});
console.log("End");
// Start
// End
// Promise

// Example 3: Promise vs setTimeout
console.log("Start");
setTimeout(() => {
    console.log("Timeout");
}, 0);
Promise.resolve().then(() => {
    console.log("Promise");
});
console.log("End");
// Start
// End
// Promise
// Timeout

// null vs undefined
let a;
console.log(a)
// undefined

// Null
let b = null;


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
