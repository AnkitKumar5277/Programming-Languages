// template literals
let name = "Ankit";
let age = 22;
let message = `My name is ${name} and I am ${age} years old.`;
console.log(message);


// nan
console.log(0 / 0);        // NaN
console.log(Number("abc")); // NaN
console.log(Math.sqrt(-1)); // NaN

// Synchronous
console.log("Start");
function add() {
  console.log(10 + 20);
}
add();
console.log("End");
// Start
// 30
// End

// Asynchronous (Non-Blocking)
console.log("Start");
setTimeout(() => {
  console.log("Task Completed");
}, 2000);
console.log("End");
// Start
// End
// Task Completed


// setTimeout()
console.log("Start");
setTimeout(() => {
  console.log("Task Completed");
}, 2000);
console.log("End");
// Start
// End
// Task Completed

// setInterval() Example
let id = setInterval(() => {
  console.log("Hello");
}, 2000);
// (After 2 sec)
// Hello
// (After 2 sec)
// Hello
// (After 2 sec)
// Hello
// ...


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


// Array
let fruits = ["Apple", "Banana", "Mango"];
console.log(fruits);
console.log(fruits[0]); // Apple
console.log(fruits[1]); // Banana
console.log(fruits[2]); // Mango

// objects
let student = {
    name: "Ankit",
    age: 22,
    city: "Delhi"
};
console.log(student);
console.log(student.name);
console.log(student.age);
console.log(student.city);


// Callback Hell
function loginUser(callback) {
    console.log("User Logged In");
    callback();
}
function getProfile(callback) {
    console.log("Profile Fetched");
    callback();
}
function getOrders(callback) {
    console.log("Orders Fetched");
    callback();
}
loginUser(function () {
    getProfile(function () {
        getOrders(function () {
            console.log("Done");
        });
    });
});
// User Logged In
// Profile Fetched
// Orders Fetched
// Done


// classes
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  introduce() {
    console.log(`Hi, I am ${this.name}. My age is ${this.age}.`);
  }
}
const person1 = new Person("Ankit", 22);
person1.introduce();


// Shallow Copy
const user1 = {
  name: "Ankit",
  address: { city: "Delhi" }
};
const user2 = { ...user1 }; // Shallow Copy
user2.address.city = "Noida";
console.log(user1.address.city); // Noida
console.log(user2.address.city); // Noida

// Deep Copy 
const user1 = {
  name: "Ankit",
  address: { city: "Delhi" }
};
const user2 = structuredClone(user1); // Deep Copy
user2.address.city = "Noida";
console.log(user1.address.city); // Delhi
console.log(user2.address.city); // Noida


// call()
const person = {
  name: "Ankit"
};
function greet(city) {
  console.log(`Hi ${this.name} from ${city}`);
}
greet.call(person, "Delhi");
// Output:
// Hi Ankit from Delhi

// apply()
const person = {
  name: "Ankit"
};
function greet(city, country) {
  console.log(`Hi ${this.name} from ${city}, ${country}`);
}
greet.apply(person, ["Delhi", "India"]);
// Output:
// Hi Ankit from Delhi, India

// bind()
const person = {
  name: "Ankit"
};
function greet() {
  console.log(`Hi ${this.name}`);
}
const newGreet = greet.bind(person);
newGreet();
// Output:
// Hi Ankit
