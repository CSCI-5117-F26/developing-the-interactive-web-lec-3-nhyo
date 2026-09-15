const button = document.querySelector("#addGuest");
const input = document.querySelector("#guestName");
const list = document.querySelector("#guestList");

button.addEventListener("click", async function () {

    const name = input.value;

    const response = await fetch("/guestbook", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            guestName: name
        })
    });

    const data = await response.json();

    const li = document.createElement("li");
    li.textContent = data.guestName;

    list.appendChild(li);

    input.value = "";
});