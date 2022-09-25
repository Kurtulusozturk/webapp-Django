var count=0;
function myFunction(x) {
  // x.classList.toggle("fa-thumbs-down");
  count=count+1;
  if (count%2 == 1){
    var styles = `
                .fa {
          font-size: 30px;
          cursor: pointer;
          user-select: none;
          color: rgb(68, 233, 68);
          }
      `
  }
  else{
    var styles = `
                .fa {
          font-size: 30px;
          cursor: pointer;
          user-select: none;
          color: rgb(212, 211, 211);
          }
      `
      count=0;
      }

    var styleSheet = document.createElement("style")
    styleSheet.innerText = styles
    document.head.appendChild(styleSheet)

}