// Arrow Function 

const add = (a, b) => a + b;
console.log(add(5,3));
// 8


const person = {
  name: "Ankit",
  normalFunction: function () {
    console.log("Normal:", this.name);
  },
  arrowFunction: () => {
    console.log("Arrow:", this.name);
  }
};
person.normalFunction();
person.arrowFunction();
// Normal: Ankit
// Arrow: undefined
