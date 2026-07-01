// Select elements

// Select Element by ID
const heading = document.getElementById("title");
console.log(heading);

// Select Element by Class
const message = document.querySelector(".message");
console.log(message);

// Select All Elements
const divs = document.querySelectorAll("div");
divs.forEach((div) => {
    console.log(div.innerText);
});

// Get Text
const title = document.getElementById("title");
console.log(title.innerText);

// Click Button
const button = document.getElementById("btn");
button.click();

// Set Input Value
const input = document.getElementById("username");
input.value = "Ankit";
console.log(input.value);

// Change Text
const paragraph = document.getElementById("demo");
paragraph.innerText = "Updated Text";

// Get Text Content
const para = document.getElementById("demo");
console.log(para.textContent);

