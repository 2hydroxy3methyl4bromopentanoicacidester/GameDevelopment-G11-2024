//scroll increment number inputs
mx = 0;
my = 0;

document.onmousemove = function(mouseEv){
    mx = mouseEv.clientX;
    my = mouseEv.clientY
}

window.onscroll = function(){
    element = document.elementFromPoint(mx, my);
    if(element.tagName == "input"){
        console.log("scroll")
    }
    console.log("scroll")
}
document.querySelectorAll("input[type='number']").forEach(e=>{
    console.log(e)
    e.addEventListener("wheel", function(event){
        val = parseFloat(e.value)
        console.log(val, Object.is(val, NaN))
        if (Object.is(val, NaN))
            val = 0
        step = 1;
        if (event.deltaY < 0) {
            e.value = val + step;
            console.log("scrolled up, value:", parseFloat(e.value));
        } else {
            e.value = val - step;
            console.log("scrolled down, value:", parseFloat(e.value));
        }
        event.preventDefault();
    })
})