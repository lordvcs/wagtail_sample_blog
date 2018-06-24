$(document).ready(function() {
  $(".markdown .field-content textarea").each(function(index, elem) {
      var mde = new SimpleMDE({
          element: elem,
          autofocus: false
      });
      mde.render();
  });
});