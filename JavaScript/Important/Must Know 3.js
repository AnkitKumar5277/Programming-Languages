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


<!DOCTYPE html>
<html>
<head>
    <title>DOM Example</title>
</head>
<body>
<h1 id="title">Hello World</h1>
<button id="btn">Click Me</button>
<script>
    const button = document.getElementById("btn");
    button.addEventListener("click", function () {
        document.getElementById("title").textContent = "Button Clicked!";
    });
</script>
</body>
</html>

