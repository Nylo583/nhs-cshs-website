function scroll2top() {
    const b = document.getElementById("scrollTop");
    const top = document.getElementById("navbar");
    b.addEventListener("click", (event) => {
        top.scrollIntoView({behavior: "smooth"});
    });
}