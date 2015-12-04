//console.log('main.js working!');

// function showCommentFormEvent(list, event, f) {
//      [].forEach.call(list, function(item) {
//           item.addEventListener(event, f);
//       });
//   }
//
// showCommentFormEvent(document.getElementsByClassName("show-comment-form"), 'click', function(event) {
//     //console.log("Button clicked");
//     event.preventDefault();
//
// });

function showCommentsFunction() {
    "use strict";
    var allComments = document.getElementById("comments");
    allComments.addEventListener("click", function(event) {

        var idJustNumber = event.target.id.slice(-1);

        if (event.target.className === "show-comment-form") {
            //should document be allComments?
            var form = document.getElementById("comment-form-"+idJustNumber);
            form.classList.add("shown");
        }
    });
}

document.addEventListener("DOMContentLoaded", function() {
    "use strict";
    if (document.getElementById('body').className === "comments") {
        showCommentsFunction();
    }
});
