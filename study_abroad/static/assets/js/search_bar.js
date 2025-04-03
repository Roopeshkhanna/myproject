document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.querySelector(".form-control.ps-5");
    const universityCards = document.querySelectorAll(".col-md-6.mb-3");

    searchInput.addEventListener("keyup", function () {
        const searchTerm = searchInput.value.toLowerCase();

        universityCards.forEach(card => {
            const universityName = card.querySelector("h5").textContent.toLowerCase();
            if (universityName.includes(searchTerm)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    });
});