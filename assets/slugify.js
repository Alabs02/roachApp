 const titleInput = document.querySelector('input[name=title]');
 const slugInput = document.querySelector('input[name=slug]');
 
 const slugify = (val) => {
     return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')         // replae & with -and
        .replace(/[\s\W-]+/g, '-')    // replace spaces, none word chars with a sinle dash

 };

 titleInput.addEventListener('keyup', (e) => {
     slugInput.setAttribute('value', slugify(titleInput.value));

 });