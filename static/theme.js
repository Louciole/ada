function initTheme(){
    const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
    if (prefersDarkScheme){
        document.body.classList.remove("light-theme");
        document.body.classList.add("dark-theme");

    }else{
        document.body.classList.add("light-theme");
        document.body.classList.remove("dark-theme");
    }
}
