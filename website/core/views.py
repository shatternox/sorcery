from flask import render_template, render_template_string, request, Blueprint
from website.core.ocrCustomBambang import get_img_string
from website.core.utils import downloadImage
from secrets import token_hex
import os


core = Blueprint('core', __name__)


@core.route("/", methods=["GET", "POST"])
@core.route("/index", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        image_link = request.form.get("image-link")

        downloaded_image = downloadImage(image_link)

        image_name = token_hex(16) + ".jpg"
        image_path = f"./website/static/images/{image_name}"

        f = open(image_path, "wb")
        f.write(downloaded_image)

        f.close()

        text_result = get_img_string(image_path)

        return render_template_string(f'''
        
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <link rel="stylesheet" href="../static/css/index.css">
  <title>Sorcery</title>
</head>
<body>
  <div class="d-flex flex-column header-result">
    <div class="d-flex w-100 justify-content-center align-self-center text-white">
      <h1>Wow.. What Sorcery Is This?</h1>
    </div>
    <h2 class="text-center">{text_result}</h2>
  </div>
  <form action="/index" method="POST">
    <div class="search-box">
      <input type="text" class="search-txt" name="image-link" placeholder="Try to Put Something, maybe a link?">
      <button type="submit" class="search-btn">
      <ion-icon name="search-outline"></ion-icon>
    </div>
  </form>
  <!-- Ionic Icons -->
  <script type="text/javascript" src="https://unpkg.com/ionicons@6.0.1/dist/ionicons.js"></script>
  <!-- Boostrap -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
</body>
</html>
        ''')

    return render_template('index.html')
