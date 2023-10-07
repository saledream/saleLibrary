function download_file(slug) {
    var url = "/books/download/" + slug + '/'
    var ajax = new XMLHttpRequest()
    ajax.open("GET",`${url}`)
    ajax.send()
    ajax.onreadystatechange = function () {

        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText)
        }
    }
}