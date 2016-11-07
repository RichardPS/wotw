<!DOCTYPE html>
<html>
  <head>

    <title>Website of the Week | PrimarySite</title>

    <link href="landing-page.css" rel="stylesheet">
    <link href="jquery.fancybox.css" rel="stylesheet">

    <script src="jquery-3.1.1.min.js"></script>
    <script src="jquery.fancybox.js"></script>
    <script src="landing-page.js"></script>

  </head>
  <body total-votes="{{ total_votes }}">

    % for item in site_data:
    <div class="site-block">
        <div class="info-block">
          <div class="vote">
            <a class="vote-link" data-fancybox-type="iframe" href="/vote/{{ item['site-uid'] }}/{{ item['site-votes'] }}"></a>
          </div>
          <div class="names-block">
            <div class="school-name">{{ item['school-name'] }}</div>
            <div class="designer-name">{{ item['designer-name'] }}</div>
          </div>
        </div>
        <div class="image-block">
            <a href="{{ item['site-url'] }}" target="_blank"><img src="{{ item['site-thumb'] }}" alt="{{ item['school-name'] }}" height="188px" width="250px" ></a>
        </div>
        <div class="votes-block">{{ item['site-votes'] }}</div>
    </div>
    % end

  </body>
</html>
