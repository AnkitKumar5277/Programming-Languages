var a = 10; // global scope

console.log(a);
function printHello() {
  console.log("Hello TheTestingAcademy!");
  var a = 20; //local scope
  console.log(a);

  if(true) {
    var a = 30;
    console.log(a);
  }
}

printHello();
var a=50;
