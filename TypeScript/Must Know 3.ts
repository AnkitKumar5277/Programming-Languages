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
user.name = "Rahul";
user.id = 102;
