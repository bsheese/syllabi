# coding: utf-8
template_textb = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ course_info['course_abrv'] }}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <!-- Bootstrap JS and Popper.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>

</head>
<body>
    <center>
    <h1>{{ course_info['title'] }}</h1>
    <h2>{{ course_info['course_abrv'] }}</h2>
    <h2>{{ semester }}</h2>
    </center>


    {% for i in body_content %}
      <p><hr><hr>
      {% set section_title, content_dic, display_instructions = i %}

      <h1>{{ section_title }}</h1>

      {% if display_instructions == 'bulleted_list' %}
        {% for key, value in content_dic.items() %}
          <li>{{key}}: {{value}}</li>
        {% endfor %}

      {% else %}
        {% for key, value in content_dic.items() %}
          {% if key in ['title', 'course_abrv'] %}
            {# pass #}
          {% elif ((key == 'Work Load') and (omit_breakdown == True)) %}
            {# pass #}
          {% else %}
            <h2>{{ key }}</h2>
            {{ value }}<br><br>
          {% endif %}
        {% endfor %}

      {% endif %}
      </p><br><br>
    {% endfor %}




    {# a comment #}
</body>
</html>
'''