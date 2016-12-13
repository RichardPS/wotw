<!DOCTYPE html>
<html>
  <head>

    <title>Website of the Week | PrimarySite</title>

    <link href="admin.css" rel="stylesheet">
  </head>
  <body>
    <section class="container">

      <section class ="header"></section>

      <section class="content">

        <p>These Sites Will Be Archived</p>

        <table class="current-sites-table archive-list">
          <tr>
            <th>Thumbnail Link</th>
            <th>School Name</th>
            <th>Designer Name</th>
            <th>Number of Votes</th>
          </tr>

          % for item in site_data:

          <tr>
            <td><a href="{{ item['site-url'] }}" target="_blank"><img src="{{ item['site-thumb'] }}" alt="{{ item['school-name'] }}" height="63px" width="83px" ></a></td>
            <td>{{ item['school-name'] }}</td>
            <td>{{ item['designer-name'] }}</td>
            <td>{{ item['site-votes'] }}</td>
          </tr>

          % end

        </table>

        <form name="contine-archiving" method="post" action="/continue-archive">
          <input type="hidden" name="winner" value="{{ winner['site-uid'] }}">
          <input type="submit" class="archive" value="Continue Archive">
        </form>

      </section>
    </section>
  </body>
</html>
