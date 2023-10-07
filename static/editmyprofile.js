window.addEventListener("load",function (){
   var file = null;
   var para = document.querySelector("#profile_photo-clear_id").parentElement;
  for(element of para.children) {
    
    if(element.name == "profile_photo"){
        element.addEventListener("change", function (){
 
              const files = this.files[0];
              var imgPreview = document.querySelector(".photo img");

              if(files) {
                const fileReader = new FileReader();
                fileReader.readAsDataURL(files);
                fileReader.addEventListener("load",function (){
                    imgPreview.src=this.result;
                    imgPreview.style.width = "100%";
                }); 

              }
        });

        file = element;
        
        
    }
    else {
        para.removeChild(element);
    }
  }
  para.innerHTML = "";
  para.appendChild(file)
  
});