// Generic
function show<T>(value: T): T {
  return value;
}
console.log(show(10));
console.log(show("Ankit"))
console.log(show(true));
// 10
// Ankit
// true

// Tuples
let user: [string, number] = ["Ankit", 22];
console.log(user[0]); 
console.log(user[1]);
// Ankit
// 22

// Readonly keyword
interface User {
  readonly id: number;
  name: string;
}
const user: User = {
  id: 101,
  name: "Ankit"
};
console.log(user.id);
user.name = "Rahul"; // ✅ Allowed
// user.id = 102; // ❌ Error
// 101

// public (default)
class Person {
  public name: string = "Ankit";
}
const p = new Person();
console.log(p.name);
// Ankit

// private
class Person {
  private age: number = 22;
  showAge() {
    console.log(this.age);
  }
}
const p = new Person();
p.showAge();      // 22
// console.log(p.age); // ❌ Error
// 22

// Protected
class Person {
  protected city: string = "Delhi";
}
class Student extends Person {
  showCity() {
    console.log(this.city);
  }
}
const s = new Student();
s.showCity(); // Delhi
// console.log(s.city); // ❌ Error


