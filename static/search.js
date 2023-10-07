class bookDiv {

    constructor(img,slug,title,page,size,language,file_type){

            this.img = img;
            this.slug = slug;
            this.title = title;
            this.page=page;
            this.language = language;
            this.size = size;
            this.f_type = file_type;
    }
    div() {

            var div = document.createElement("div");

       return div;     
    }
    link(){

        
        var a_link = document.createElement("a");
        
        a_link.href = "/books/book-detail/" + this.slug;
        
        return a_link;
        
    }
    imgE() {
        var image = document.createElement("img");
        image.setAttribute("src",this.img)
        image.style.width = "100%";
        return image;
    }
    book_cover() {

        
        var container = this.div();
            container.setAttribute("class","book-cover");
        var a_link = this.link();
        a_link.appendChild(this.imgE());
        
        container.appendChild(a_link);

        return container;
    }
    para(label,value) {

            var span = document.createElement("span");
            var para = document.createElement("p");
            span.innerHTML = label;
            para.appendChild(span);
            para.append(value);
            

       return para;     
    }
    book_data() {
          var container = this.div();
             container.setAttribute("class","metadata");
           container.appendChild(this.para("Title:",this.title));
           container.appendChild(this.para("Pages:",this.page));
           container.appendChild(this.para("Size:",this.size));
           container.appendChild(this.para("Language:",this.language));
           container.appendChild(this.para("File type:",this.f_type));

          return container;

    }
    book() {
        var container = this.div();
        container.setAttribute("class","book-container");

        container.appendChild(this.book_cover());
        container.appendChild(this.book_data());
        return container;
    }
}



function search_book() {

    var  textinput = document.querySelector("input[type='search']");
    var  searchbutton = document.querySelector("input[type='button']");
    var txt_list = textinput.value.split(" ");
    var search_term = txt_list.join("+");

    ajax(search_term);


}

function ajax(value) {

    var ajax = new XMLHttpRequest()
    ajax.open("GET","/books/search?q="+value);
    ajax.send();

    ajax.onreadystatechange = function () {

        if(this.readyState == 4 && this.status == 200){
                var result = 0;
                var data_list = JSON.parse(this.responseText)
                var grid_books = document.querySelector(".grid-books");
                var book_cover = document.querySelectorAll(".grid-cover");

                console.log(grid_books.children);
                console.log(book_cover);
                book_cover.forEach(div =>{

                    grid_books.removeChild(div);
                });

                for(dc of data_list) {


                     grid_books.appendChild(new bookDiv(dc.cover,dc.slug,dc.title,dc.page,dc.size,dc.language,dc.file_type).book())
                     result = result + 1;
                }
                document.querySelector("#result").innerHTML = ` about ${result} search results`;
                grid_books.style.display ="block";  
                // bookDiv instance
                console.log(data_list[0]);
        }
        else {
            ;
        }
    }
}