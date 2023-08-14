// for topscrool button

const toTop = document.querySelector(".to-top");

window.addEventListener("scroll",() =>{
    if (window.pageYOffset > 120) {
        toTop.classList.add("active");
    }
    else{
        toTop.classList.remove("active");
    }
})


function setMainImage(image) {
    var mainImage = document.getElementById('main-image');
    mainImage.src = image.src;
    mainImage.alt = image.alt;
  }
  
// for upload image

function getImagePreview(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);

    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }
  
function getImagePreview2(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview2');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);


    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }

function getImagePreview3(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview3');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);


    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }
  
  function getImagePreview4(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview4');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);


    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }

  function getImagePreview5(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview5');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);


    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }

  function getImagePreview6(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview6');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);


    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }

  function getImagePreview7(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview7');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);


    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }

  function getImagePreview8(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview8');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);


    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }

  function getImagePreview9(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview9');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);


    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }

  function getImagePreview10(event, nextPreview)
  {
    var image=URL.createObjectURL(event.target.files[0]);
    var imagediv= document.getElementById('preview10');
    var newimg=document.createElement('img');
    imagediv.innerHTML='';
    newimg.src=image;
    newimg.width="119";
    newimg.height="100";
    imagediv.appendChild(newimg);


    var nextImagediv= document.getElementById(nextPreview);
    nextImagediv.style.display = "block";
    var nextUploadBtn= nextImagediv.nextElementSibling;
    nextUploadBtn.style.display = "flex";
  }




// // Enable Bootstrap dropdowns For deep dropdown
// var dropdowns = document.querySelectorAll('.dropdown-toggle');
// dropdowns.forEach(function(dropdown) {
//   new bootstrap.Dropdown(dropdown, {
//     hover: true
//   });
// });

