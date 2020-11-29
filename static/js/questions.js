function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
//get csrf
const csrftoken = getCookie('csrftoken');

$('.js-vote-btn').on('click',function(post){
  if ($(this).hasClass('up')){
        method = 'up'
  } else {
        method = 'down'
  }
  post.preventDefault();
  $.ajax({
    type: 'POST',
    url: '/question/rate/',
    data: {
       'method':method,
       'questionPk': questionPk,
       csrfmiddlewaretoken: csrftoken,
    },
    dataType: 'JSON',
    success: function(data){
    console.log(data.rating)
         $('.rating').text(data.rating);
         },
    error: function(data){
           console.log(data)
    }

   }
  );
});

