/* Check whether backdrop filter is supported */
var bdFilterSupport = CSS.supports('backdrop-filter', 'blur(10px)');

/* If backdrop filter is supported, edit each element to be transparent and to have backdrop filter */
if(bdFilterSupport) {
  var re = /(rgb)\(([0-9]+),\s+([0-9]+),\s+([0-9]+)/; // TODO: what does happen if RGBA color is input?
  var elems = document.getElementsByClassName('acryl');
  for(i = 0; i < elems.length; i++) {
    let color = window.getComputedStyle(elems[i]).backgroundColor;
    var subst = 'rgba($2,$3,$4,0.85'; 
    color = color.replace(re, subst);
    elems[i].style.backgroundColor = color;
    elems[i].style.backdropFilter = 'blur(10px)';
  }
}