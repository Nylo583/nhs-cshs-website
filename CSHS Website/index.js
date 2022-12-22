function scroll2top() {
    const b = document.getElementById("scrollTop");
    const top = document.getElementById("navbar");
    b.addEventListener("click", (event) => {
        top.scrollIntoView({behavior: "smooth"});
    });
}

function scrollPost() {
    const button = document.getElementById("rcn");
    const post0 = document.getElementById("post0");
    button.addEventListener("click", (event) => {
        post0.scrollIntoView({behavior: "smooth"});
    });
}

