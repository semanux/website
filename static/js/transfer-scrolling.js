/* Get scroll offset from URL parameters and apply it */
const urlParams = new URLSearchParams(window.location.search);
const scrollOffset = urlParams.get('s');
window.scrollTo(0, scrollOffset);

/* Adapt language switches to call URL with scroll offset as parameter */
var languageSwitches = document.getElementsByName('language_switch');
for (let item of languageSwitches) {
    var href = item.href;
    item.setAttribute('href', '#');
    item.setAttribute('onclick', 'window.open("' + href + '?s=\"+Math.floor(window.scrollY)+\"", "_self");');
}