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
