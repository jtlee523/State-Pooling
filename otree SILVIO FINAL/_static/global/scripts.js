
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
    var slider = document.getElementById(id_slider); //$(slider_id)
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

//MY FUNCTIONS BELOW =============================
function getSliderValuesStatic(id_slider) {
    var mySlider = document.getElementById(id_slider); //calls in the slider as a variable
    var valueString = document.getElementById(id_slider).value; //reads off the array
    //var valueArray = mySlider.getValue(); //this doesn't seem to work
    
    console.log("ValueString is: " + valueString);
    //console.log(typeof valueArray); //typeof returns the type ///string
    
    var NumArray = valueString.split(','); //splits by column
    console.log("NumArray is: " + NumArray);
    //console.log(typeof NumArray);
    
    var FirstNum = NumArray[0]; //index by []
    var SecondNum = NumArray[1]; 
    
    console.log("FirstNum is: " + FirstNum);
    console.log("SecondNum is: " + SecondNum);
    

}
//===========Below are my functions. The bottom most one is the one I have primarily been working with

//This function is a test that I messed with to get dynamic values
//it did not work

//THIS ONE WORKS======
function getSliderValues(slider_name){ //doesn't work
	 
	var valueString = slider_name.value;
    console.log("(FROM INTERNAL) Static ValueString is: " + valueString);
    	
    var NumArray = valueString.split(','); //splits by column
    console.log("(FROM INTERNAL) NumArray is: " + NumArray);
    
   	var FirstNum = NumArray[0];
    var SecondNum = NumArray[1]; 
    
   	console.log("(FROM INTERNAL) FirstNum is: " + FirstNum);
    console.log("(FROM INTERNAL) SecondNum is: " + SecondNum);
    	
    }


    
    
//I would like this function to dynamically update.
function getSliderValuesDynamic(id_slider) {
    var mySlider = $(id_slider) 
    console.log("step1");
    console.log(mySlider);
    //document.getElementById(id_slider); //calls in the slider as a variable
    mySlider.on('slide',function(){
    	var valueString = this.value;
    	console.log("Static ValueString is: " + valueString);
    	
    	var NumArray = valueString.split(','); //splits by column
    	console.log("NumArray is: " + NumArray);
    	
    
   	 	var FirstNum = NumArray[0];
   		var SecondNum = NumArray[1]; 
    
   		console.log("FirstNum is: " + FirstNum);
    	console.log("SecondNum is: " + SecondNum);
    })

}






function ChangeValue(Probability, id_bar) {
    //var slider = document.getElementById(id_slider); //$(slider_id)
    var bar = document.getElementById(id_bar);
    console.log("MADE IT HERE");
    bar.style.width = (Probability) + 'px';
    }
    
    
    
