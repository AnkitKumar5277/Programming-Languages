// Callback Function
function greet(name, callback) {
  console.log("Hello", name);
  callback();
}
function sayBye() {
  console.log("Goodbye!");
}
greet("Ankit", sayBye);
// Hello Ankit
// Goodbye!

