
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
