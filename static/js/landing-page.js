$(function(){

  $('.vote-link').fancybox({
    type: 'iframe',
    scrolling: 'no',
    fitToView: false,
    width: '80%',
    height: 'autoSize',
    autoHeight: true,
    autoSize: true,
    closeClick: true,
    openEffect: 'none',
    closeEffect: 'none',
    iframe: {
      preload: true
    }
  });

  var total_votes;
  total_votes = $('body').attr('total-votes');

  $('.votes-block .vote-number').each(function(){
    var site_votes = $(this).text();
    if(total_votes != 0){
      this_percent = Math.round((site_votes / total_votes) * 100);
      //$(this).parent().children('.vote-background').css('background','linear-gradient(to right, #009FE4 0%,#009FE4 ' + this_percent + '%,#ffffff ' + this_percent + '%)');
      $(this).parent().children('.vote-background').animate({
        width: this_percent + '%'
      }, 2000);
    }else{
      this_percent = 0
    }
    //console.log(this_percent);
    new_text = this_percent + "%";

    $(this).text(new_text);
  });

  console.log(total_votes);

});
