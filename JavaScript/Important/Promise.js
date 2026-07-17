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

