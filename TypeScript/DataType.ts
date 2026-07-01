// String Array
let users: string[] = ["Ankit", "Rahul", "Amit"];
console.log("Users:", users);

// Number Array
let ids: number[] = [1, 2, 3];
console.log("IDs:", ids);

// Access Array Element
console.log("First User:", users[0]);
console.log("Second ID:", ids[1]);

// Add New Element
users.push("Rohit");
numbers.push(40);
console.log("After Push:");
console.log(users);
console.log(numbers);

// Remove Last Element
users.pop();
console.log("After Pop:");
console.log(users);

// Loop Through Array
console.log("All Users:");
for (let user of users) {
    console.log(user);
}
