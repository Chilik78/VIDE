
$('#input0').click(function() {
 if($("select#input0 :selected").val() == "rus") {
    $("select#input0").attr('style', 'background-image:url(images/lng_ru.png);');
 }
 if($("select#input0 :selected").val() == "eng") {
    $("select#input0").attr('style', 'background-image:url(images/lng_eng.png);');
 }
    console.log('select color: '+$("select#input0 :selected").val());
});
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Закройте выпадающее меню, если пользователь щелкает за его пределами
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }