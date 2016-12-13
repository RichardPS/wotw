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
        <h2>All Active Users</h2>
        % if len(user_data) > 0:

          <table class="current-sites-table">
            <tr>
              <th>User Name</th>
              <th>Number of Times Voted</th>
              <th>Remove User</th>
            </tr>

            % for item in user_data:

            <tr>
              <td>{{ item['user_firstname'] }} {{ item['user_surname'] }}</td>
              <td>{{ item['user_total_votes'] }}</td>
              <td>
                <form action="#" name="delete-user">
                  <input type="hidden" name="user-id" value="{{ item['user_id'] }}"/>
                  <span class="delete-user"><input type="submit" value="+"/></span>
                </form>
              </td>
            </tr>

            % end

        % else:
          <p>No active users</p>
        % end

        </table>

      </section>
    </section>
  </body>
</html>
