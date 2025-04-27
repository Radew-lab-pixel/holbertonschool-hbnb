async function populatePlaces() {
    try {
        const response = await fetch("http://localhost:5001/api/v1/places", {
            method: "GET",
        });
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log("Fetched places:", data);

        for (const place of data) {
            const card = document.createElement("div");
            card.className = "place-card";

            const h1 = document.createElement("h1");
            h1.innerHTML = place.title;

            const img = document.createElement("img");
            img.src = `/static/images/${place.image}`;  // Use the image from the API
            img.alt = "House Image";

            const p = document.createElement("p");
            p.innerHTML = `AU $<span class='price'>${place.price}</span> per night`;

            const a = document.createElement("a");
            a.className = "details-button";
            a.innerHTML = "View Details";
            a.href = `/place?place_id=${place.id}`;

            card.appendChild(h1);
            card.appendChild(img);
            card.appendChild(p);
            card.appendChild(a);

            document.getElementById("places-list").appendChild(card);
        }

        return data;
    } catch (error) {
        console.error("Error fetching places:", error);
        return [];
    }
}

document.addEventListener("DOMContentLoaded", async () => {
    await populatePlaces();

    const filterElement = document.getElementById("price-filter");

    filterElement.addEventListener("change", (e) => {
        const maxPrice = Number(e.target.value.trim());

        const placesList = document.getElementById("places-list");

        placesList.querySelectorAll(".place-card").forEach((card) => {
            const priceTag = card.querySelector(".price");

            const price = Number(priceTag.innerHTML.trim());

            if (price > maxPrice) {
                card.style.display = "none";
            } else {
                card.style.display = "block";
            }
        });
    });
});