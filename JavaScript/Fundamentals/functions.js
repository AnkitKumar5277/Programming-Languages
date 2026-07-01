
// Function Declaration 
function greet(name) {
    return `Hello, ${name}!`;
}
console.log(greet("Ankit"));

// Arrow Functions (Modern) 
const greetArrow = (name) => `Hello, ${name}!`;
console.log(greetArrow("John"));

// Default Parameters 
function greetDefault(name = "Guest") {
    console.log(`Hello, ${name}!`);
}

greetDefault();        // Guest
greetDefault("Sam");    // Sam

// Hello, Ankit!
// Hello, John!
// Hello, Guest!
// Hello, Sam!
