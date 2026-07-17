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
