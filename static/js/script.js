let searchButton = document.getElementById("search_button");


searchButton.addEventListener("click", searchBar);


function searchBar(){
    let searchContainer = document.getElementById("search_container")
    if (searchContainer.classList.contains('hidden')){
        searchContainer.classList.remove("hidden");
    }
    else{
        searchContainer.classList.add("hidden")
    }
    
}