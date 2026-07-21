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

