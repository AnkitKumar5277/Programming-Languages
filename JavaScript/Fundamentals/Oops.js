// Inheritance
class Browser {
   open() {
       console.log("Browser Opened");
   }
}
class Chrome extends Browser {
   launch() {
       console.log("Chrome Launched");
   }
}
