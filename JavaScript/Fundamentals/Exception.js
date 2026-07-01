try {
    let x = y; // y is not defined
    console.log(x);
} catch (err) {
    console.log("Error:", err);
}

// Try Catch
let age = 15;
try {
    if (age < 18) {
        throw new Error("You are not eligible to vote.");
    }
    console.log("You can vote.");
} catch (error) {
    console.log("Error:", error.message);
}
// ERROR!
// Error: You are not eligible to vote.
