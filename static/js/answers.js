$('#answerForm').on('submit',function(post){
  post.preventDefault();
  $.ajax({
    type: 'POST',
    url: '/answers/create_answer/',
    data: {
       'questionPk': questionPk,
       'text': $('#answerText').val(),
       csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },
    dataType: 'html',
    success: function(data){
         $('#answerList').prepend(data);
         $('#answerText').val('');
         },
    error: function(data){
           console.log(data)
          $('#answerText').val(data['responseText']);
    }

   }
  );
});

