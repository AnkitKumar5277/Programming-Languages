// Type Interence
let name = "Ankit";
console.log(name); // Ankit

// Arrow functions 
const add = (a:number, b:number): number => {
  return a +b;
};
console.log(add(5,4));
// 9

// What are Modules
// math.ts
export function add(a: number, b: number): number {
    return a + b;
}
// app.ts
import { add } from "./math";
console.log(add(10, 20));
Output
// 30

// optional parameters
function greet(name: string, city?: string) {
  console.log(name);
}

// void
function greet(): void{
  console.log("hello");
}
console.log(greet());
// hello
// undefined

// Intersection type
type A = {  name: string;  };
type B = {  age: number;  };
type Person = A & B;
const person: Person = {
  name: "Ankit",
  age: 22
};
console.log(person);

// Nullish Coalescing (??)
let userName = null;
let name = userName ?? "Guest";
console.log(name);
// Guest

// Optional Chaining (?.)?
const user = {
  name: "Ankit",
  address: {
    city: "Delhi"
  }
};
console.log(user?.address?.city);
// Delhi

// never
function throwError(): never {
  throw new Error("Something went wrong!");
}

// Literal Type
let direction: "left" | "right";
direction = "left";   // ✅ Valid
direction = "right";  // ✅ Valid
console.log(direction);
// right
