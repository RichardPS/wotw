<!DOCTYPE html>
<html>
  <head>
    <link href="landing-page.css" rel="stylesheet">
  </head>
  <body>

    % for item in site_data:
    <div class="site-block">
        <div class="info-block">
          <div class="vote">
            <a href="/vote/{{ item['site-id'] }}"></a>
          </div>
          <div class="names-block">
            <div class="school-name">{{ item['school-name'] }}</div>
            <div class="designer-name">{{ item['designer-name'] }}</div>
          </div>
        </div>
        <div class="image-block">
            <img src="{{ item['site-thumb'] }}" alt="{{ item['school-name'] }}" height="188px" width="250px" >
        </div>
        <div class="votes-block">{{ item['site-votes'] }}</div>
    </div>
    % end

  </body>
</html>
