<!DOCTYPE html>
<html>
  <head>
    <link href="../../voting-page.css" rel="stylesheet">
  </head>
  <body>
    % for item in voters:
      <div class="voter">
        <a href="../../voted_for/{{ item[0] }}/{{ site_uid }}/{{ item[4] }}/{{ site_votes }}" target="_parent">
          <img src="../../user.png" height="64px" width="64px">
          <p>{{ item[3] }}</p>
        </a>
      </div>
    % end
  </body>
</html>
