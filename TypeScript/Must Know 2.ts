// Optional Property
interface User {
  name: string;
  age?: number;
}
const user1: User = {
  name: "Ankit",
  age: 22
}
const user2: User = {
  name: "Rahul"
};
console.log(user1);
console.log(user2);
// { name: 'Ankit', age: 22 }
// { name: 'Rahul' }

// Union Type
let value: string | number;
value = "Ankit";
console.log(value); // Ankit
value = 25;
console.log(value); // 25
value = true;
// Ankit
// 25

// Function Type
function add(a: number, b: number): number {
  return a + b;
}
console.log(add(10, 20));
// 30

// Type Assertion
let value: any = "Hello TypeScript";
let text = value as sring;
console.log(text.length);
// 16

// Enum
enum Status {
  Pass,
  Fail
}
let result: Status = Status.Pass;
console.log(result);
console.log(Status.Pass);
console.log(Status.Fail);
// 0
// 0
// 1
