$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-program .modal-content").html("");
        $("#modal-program").modal("show");
      },
      success: function (data) {
        $("#modal-program .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#program-table tbody").html(data.html_program_list);
          $("#modal-program").modal("hide");
        }
        else {
          $("#modal-program .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create program
  $(".js-create-program").click(loadForm);
  $("#modal-program").on("submit", ".js-program-create-form", saveForm);

  // Update program
  $("#program-table").on("click", ".js-update-program", loadForm);
  $("#modal-program").on("submit", ".js-program-update-form", saveForm);

  // Delete program
  $("#program-table").on("click", ".js-delete-program", loadForm);
  $("#modal-program").on("submit", ".js-program-delete-form", saveForm);

});
