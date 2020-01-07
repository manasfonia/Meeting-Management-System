 $(function () {
        $('#datetimepicker7').datetimepicker();
        $('#datetimepicker8').datetimepicker({
            useCurrent: false
        });
        $("#datetimepicker7").on("change.datetimepicker", function (e) {
            $('#datetimepicker8').datetimepicker('minDate', e.date);
        });
        $("#datetimepicker8").on("change.datetimepicker", function (e) {
            $('#datetimepicker7').datetimepicker('maxDate', e.date);
        });
    });

















function getval(sel, )
{
 $.ajax({
    url: '/accounts/profile/getdata/'+ sel.value,
    type: "GET",
    data: "response",
    dataType: "json",
    success: function(data) {
            document.getElementById("upcoming-meetings").innerHTML='<object type="type/html" data="upcoming_meetings.html" ></object>';
//            $("#upcoming-meetings").load('upcoming');
//            insertAdjacentHTML("upcoming-meeting ", "<h3>This is the text which has been inserted by JS</h3>");
            alert("Thank you for the response");
        },
    error: function (data) {
          alert("Error" + sel.value);
      }
  });
  alert(sel.value);

}
