<!DOCTYPE html>
<html>
  <head>

    <title>Website of the Week | PrimarySite</title>

    <link href="admin.css" rel="stylesheet">
  </head>
  <body>
    <section class="container">

      <section class ="header"></section>
      {{ !navigation }}
      <section class="content">

        <a href="/admin-add-site" class="add-new" alt="Add New" title="Add New">Add New</a>

        <table class="current-sites-table">
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

        % if len(site_data) > 0:
          <a href="/archive" class="archive" alt="Archive" title="Archive">Archive</a>
        % end

      </section>
    </section>
  </body>
</html>
