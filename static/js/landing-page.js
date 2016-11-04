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

});
