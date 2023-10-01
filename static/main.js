/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

// Filtering function

// filterBooks('fantasy');
function filterBooks(genre) {
  // Get all books
  var books = document.getElementsByClassName('col mb-5');

  // Loop through all books
  for(var i = 0; i < books.length; i++) {
    var book = books[i];

    // Check if the book belongs to the selected genre
    if(book.classList.contains(genre)) {
      // If it does, show the book
      book.style.display = 'block';
    } else {
      // If it does not, hide the book
      book.style.display = 'none';
    }
  }
}



// col mb-5 fantasy
// function filter(genre) {
//     var getGe = document.getElementByClass("col mb-5");
//     console.log(getGe);

//     if (getGe == fantasy) {
//         display("none");
//     } else {
//         display("block");
//     }
// }

// 1. 'col mb-5' class 들의 클래스 명을 가져오는 함수
// e.g. <div class= 'col mb-5 fantasy'></div>

// var books = document.getElementsByClassName('col mb-5')

// //2. 모든 books(variable) list의 item 을 loop로 print 하는 부분

// for(elements in py-5){
//   var book = books[i]
// }

// //3. book element가 display 되게 만들기
// // 반대로 display 되지 않게 만드는 방법은
// // book.style.display = 'none'

// book.style.display = 'none'

// function filterBooks(genre){
// var books = document.getElementsByClassName

// for(elements in py-5){

// var book = book[i]

// // 나머지 코드는 수업시간에 같이 만듭니다.

// book.style.display = 'display'

// }
// }
