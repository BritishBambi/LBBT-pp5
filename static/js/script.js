let searchButton = document.getElementById("search_button");

searchButton.addEventListener("click", searchBar);

function searchBar(){
    let searchContainer = document.getElementById("search_container")
    searchContainer.classList.remove("hidden");
}