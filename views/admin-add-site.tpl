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

        <form action="/upload-new-site" method="post" enctype="multipart/form-data" class="user-form">
          <label>School Name:<input required type="text" name="school_name"></label>
          <label>Website URL:<input required type="text" name="website_url"></label>
          <label>Designer Name:<input required type="text" name="designer_name"></label>
          <label>Site Launch Date:<input required type="date" name="launch_date"></label>
          <label>Website Screenshot:<input required type="file" name="website_screenshot" accept=".jpg"></label>
          <input type="submit" value="Start Upload" class="add-new">
        </form>

      </section>
    </section>
  </body>
</html>
