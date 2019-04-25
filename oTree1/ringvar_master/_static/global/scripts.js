
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


function setSliderValueLeft(id_left, value) {
    document.getElementById(id_left).value = value; //getElementById() seems to get the values
    //ask about a dynamic print function
}

function setSliderOutputLeft(id_left, id_output) {
    var slider = document.getElementById(id_left);
    var output = document.getElementById(id_output);
    output.innerHTML = slider.value; // Display the default slider value
    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function() {
        output.innerHTML = (this.valueAsNumber*100).toFixed(1) + '%';
    }
    slider.oninput()
    slider.focus()
}


function setUpdateBarLeft(id_left, id_bar) {
    var slider = document.getElementById(id_left);
    var bar = document.getElementById(id_bar);
    slider.oninput = function() {
        bar.style.width = (this.valueAsNumber*100).toFixed(1) + 'px';
    }
    slider.oninput()
    slider.focus()
}


//var sliderA = new Slider("#ex12a", { id: "slider12a", min: 0, max: 10, value: 5 });
//var sliderB = new Slider("#ex12b", { id: "slider12b", min: 0, max: 10, range: true, value: [3, 7] });
//var sliderC = new Slider("#ex12c", { id: "slider12c", min: 0, max: 10, range: true, value: [3, 7] }); //this is the one we want

//var slider = new Slider("#ex4", {
//	reversed : true
//}); //This is for the verticle
