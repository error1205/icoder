var script = document.createElement('script');
script.type = "text/javascript";
script.src = "https://cdn.tiny.cloud/1/e7praf2kw88zhra4e87yu801ywog0vte1yrc5gnb7p34a1uf/tinymce/5/tinymce.min.js";
document.head.appendChild(script);
script.onload = function(){
tinymce.init({
    selector: '#id_content',
    height:600,
    plugins: ['a11ychecker advcode casechange export formatpainter linkchecker autolink lists checklist media mediaembed pageembed permanentpen powerpaste table advtable tinycomments tinymcespellchecker'],
    toolbar: ['a11ycheck addcomment showcomments casechange checklist code export formatpainter pageembed permanentpen table'],
    toolbar_mode: ['floating'],
    tinycomments_mode: 'embedded',
    tinycomments_author: 'Author name',
});}
