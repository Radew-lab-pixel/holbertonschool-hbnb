
async function populatePlaces() {
    // Fetch all places
    const data = await fetch("http://127.0.0.1:5000/api/v1/places", {
        method: "GET",
    })
    .then((res) => res.json());

    console.log(data);

    for (const place of data) {
        // <div class="place-card">
        //     <!-- <h1><img src="./static/images/house1.jpg" alt="house" width="140" height="80"> House 1</h1> -->
        //     <h1><img src="{{ url_for('static', filename='images/house1.jpg') }}" alt="House 1"></h1>
        //     <p150</p>
        //     <!-- <a href="./place.html" class="details-button">View Details</a> -->
        //     <a href="./place" class="details-button">View Details</a>
        // </div>

        const card = document.createElement("div");
        card.className = "place-card";

        const h1 = document.createElement("h1");
        h1.innerHTML = place.title;

        const img = document.createElement("img");
        img.src = "/static/images/house1.jpg";
        img.alt = "House Image"

        const p = document.createElement("p");
        p.innerHTML = place.price;

        const a = document.createElement("a");
        a.className = "details-button"
        a.innerHTML = "View Details";
        a.href = `/place?place_id=${place.id}`;

        card.appendChild(h1);
        card.appendChild(img);
        card.appendChild(p);
        card.appendChild(a);

        document.getElementById("places-list").appendChild(card);
    }

    return data;
}

document.addEventListener("DOMContentLoaded", async () => {
    // Populate places
    await populatePlaces();

    const filterElement = document.getElementById("price-filter");

    filterElement.addEventListener("change", (e) => {
        const maxPrice = Number(e.target.value.trim());

        const placesList = document.getElementById("places-list");

        placesList.querySelectorAll(".place-card").forEach((card) => {
            const priceTag = card.querySelector("p");

            const price = priceTag.innerHTML.trim();

            if (price > maxPrice) {
                // Hide card
                card.style.display = "none";
            } else {
                // Show card
                card.style.display = "block";
            }
        })
    })
});