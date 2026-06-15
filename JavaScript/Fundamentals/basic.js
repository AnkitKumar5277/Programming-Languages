var xobject = {};
xObject = {
    name : "ankit",
    age : 99
}

function greet() {
    console.log("hi, how are you?")
}
greet()

var response = '{"name" : "Pramod","age" : 30,"cars" : ["Audi","BMW","I10"]}';
var parseResponseJS = JSON.parse(response)
console.log(response)

console.log(parseResonJS["name"])
var parseResponseJS = JSON.parse(response)

console.log(parseResponseJS["name"])
console.log(parseResponseJS["age"])

// JS Object -> JSON
var jsObject = {
  name : "Amit",
  age : 89
}

var JSONStr = JSON.stringify(jsObject)
console.log(JSONStr)

var xArray = ["apple","organe","bananana"]
console.log(xArray[0])
console.log(xArray[1])


xObject = {
    name: "ankit",
    age: 22
};
console.log(xObject.age, xObject.name);

xArray = ['xuv700', 'i10', 'Hector']; //indexing
console.log[xArray[1]];

// var a: boolean = 'Ankit'; // string is not assignable to number

let arrayOfObject = [
    { name: 'a', age:30},
    { name: 'b', age:22},
];
console.log(arrayOfObject[0].name, arrayOfObject[0].age);
console.log(arrayOfObject[1].name, arrayOfObject[1].age);

// switch
var day = 1;
switch(day) {
    case 1:
        console.log('Sunday');
        break;
    case 2:
        console.log('Monday');
        break;
    default:
        console.log('Not invalid date');
}

var st = "Apple, Banana, Kiwi";
console.log(st.split(', '));
console.log(st.slice(0, 4));

// var response = '{
//     "name":"Ankit", 
//     "age":23,
//     "car":["tesla", "ferrai", "Bugati"]
// }';
// const parsedJson = JSON.parse(response);    
// console.log(response.name);
// console.log(JSON.stringify(parsedJson));
