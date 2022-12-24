function scrollPost() {
    const button = document.getElementById("rcn");
    const post0 = document.getElementById("post0");
    button.addEventListener("click", (event) => {
        post0.scrollIntoView({behavior: "smooth"});
    });
}