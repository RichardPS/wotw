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
  total_votes = $('body').attr('total-votes')
  //console.log(total_votes)

  $('.votes-block').each(function(){
    var site_votes = $(this).text();
    this_percent = Math.round((site_votes / total_votes) * 100);
    //console.log(this_percent);
    new_text = this_percent + "%";
    $(this).text(new_text);
  });


});
