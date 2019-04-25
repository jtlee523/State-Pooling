
function setSliderValue(id_slider, value) {
    document.getElementById(id_slider).value = value;
}

function setSliderOutput(id_slider, id_output) {
    var slider = document.getElementById(id_slider);
    var output = document.getElementById(id_output);
    output.innerHTML = slider.value; // Display the default slider value
    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
        output.innerHTML = (this.valueAsNumber*100).toFixed(1) + '%';
    }
    slider.oninput()
    slider.focus()
}


function setUpdateBar(id_slider, id_bar) {
    var slider = document.getElementById(id_slider);
    var bar = document.getElementById(id_bar);
    slider.oninput = function() {
        bar.style.width = (this.valueAsNumber*100).toFixed(1) + 'px';
    }
    slider.oninput()
    slider.focus()
}


function makeSpaceBarSubmitForm(id_form) {
    var form = document.getElementById(id_form);
    function keyPress(e){
      var x = e || window.event;
      var key = (x.keyCode || x.which);
      if(key == 32 || key == 13 || key == 3){ // 32 is spacebar
       x.preventDefault(); // prevent spacebar from scrolling window
       form.submit();
      }
    }
    document.onkeypress = keyPress;
}
