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

