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

        <form method="post" action="/add-user-to-db" class="user-form">
          <label>Forname: <input required type="text" name="forname"></label>
          <label>Surname: <input required type="text" name="surname"></label>
          <input type="submit" class="add-new" value="continue">
        </form>

      </section>
    </section>
  </body>
</html>
