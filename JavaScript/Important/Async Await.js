// .then() aur .catch() ki jagah normal synchronous jaisa code likh sakte hain.
function getData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data received!");
    }, 2000);
  });
}

async function fetchData() {
  console.log("Fetching data...");

  let result = await getData();

  console.log(result);
}

fetchData();
