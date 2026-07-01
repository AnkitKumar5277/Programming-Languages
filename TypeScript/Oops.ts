// Interface - Can be used to make the parameters cleaner and reusable
interface User {
 name: string;
 email: string;
}
const user: User = {
 name: "Ankit",
 email: "ankit@test.com"
};

// Class
class Employee {
 name: string;
 constructor(name: string) {
   this.name = name;
 }
 display() {
   console.log(this.name);
 }
}
const emp = new Employee("Ankit");
emp.display();
