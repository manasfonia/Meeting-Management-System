function getval(sel)
{
 $.ajax({
    url: '/accounts/profile/getdata/'+ sel.value,
    type: "GET",
    data: "response",
    dataType: "json",
    success: function(data) {
            $('#upcoming-meetings').html(data.response)
        },
    error: function (data) {
          alert("Error" + sel.value);
      }
  });
}









