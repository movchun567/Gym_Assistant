//   var loadFile = function (event) {
//     var image = document.getElementById("output");
//     image.src = URL.createObjectURL(event.target.files[0]);
// };
// function loadFile(event) {
//   var reader = new FileReader();
//   reader.onloadend = function() {
//       var base64String = reader.result.replace("data:", "")
//           .replace(/^.+,/, "");

//       // send the Base64 string to the server
//       $.ajax({
//           url: '/profile_image',  // replace with the URL of your server-side script
//           type: 'POST',
//           data: { image: base64String },
//           success: function(response) {
//               // handle the response from the server
//               console.log(response);
//           }
//       });
//   }
//   reader.readAsDataURL(event.target.files[0]);
// }