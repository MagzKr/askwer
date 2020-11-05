$('#answerForm').on('submit',function(post){
  post.preventDefault();
  $.ajax({
    type: 'POST',
    url: '/answers/create_answer/',
    data: {
       'questionPk': $('#questionPk').text(),
       'text': $('#answerForm textarea').val(),
       csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },
    dataType: 'json',
    success: function(data){
         $('.commentStyle').append(data)
   }
  });
});

