template_textb = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{{ course_info['course_abrv'] }}</title>
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
            {{ value }}
          {% endif %}
        {% endfor %}

      {% endif %}
      </p>
    {% endfor %}




    {# a comment #}
</body>
</html>
'''