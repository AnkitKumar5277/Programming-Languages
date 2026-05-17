var v = 10; 
let l = 30;
const c = 3.14;
var browser = "chrome";
var browser = "firefox";
browser = "edge";

var testCases = ["login", "logout", "signup"];
for (var i = 0; i<testCases.length; i++) {
  console.log("Running test:", testCases[i]);
}

console.log("Loop counter leaked outside:", i);
console.log("Hi");
console.log("Hi");
console.log("Hi");

function say() {
  console.log("Hi from function");
}

say();
say();
