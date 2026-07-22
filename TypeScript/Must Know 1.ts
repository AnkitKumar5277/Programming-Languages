// Type Annotation
let age: number = 25;
console.log(age);
// 25

// any
let value: any = "Hello";
value = 100;
value = true;
// console.log(value); 
// 100
// true

// Unknown
let value: unknown = "Hello";
// console.log(value.toUpperCase()); // ❌ Error
if (typeof value === "string") {
console.log(value.toUpperCase()); // ✅ HELLO
}

// Interface
interface Student {
  name: string;
  age: number;
}
const student: Student = {
  name: "Ankit",
  age: 21
}
console.log(student.name);
console.log(student.age);
// Ankit
// 21

// Type Alias
type User = {
  name: string;
  age: number;
};
const user1: User = {
  name: "Ankit",
  age: 22,
};
console.log(user1.name);
console.log(user1.age);  
// Ankit
// 22
