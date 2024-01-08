from jinja2 import Environment, FileSystemLoader

import importlib
from templates import template_textb
from content import courses
from content import instructor
from content import grading
from content import policies

# modules_to_reload = ["courses", "instructor", "grading", "policies"]
#
# for module_name in modules_to_reload:
#     module = importlib.import_module(module_name)
#     importlib.reload(module)

# grabs the template as a string
template_textb = template_textb.template_textb

# write the template as a string to html
with open('templates/template1.html', 'w') as fp:
    fp.write(template_textb)

# grab dictionary of course specific information
course_dic = courses.course_dic
instructor_dic = instructor.instructor_dic
ta1_dic = instructor.ta1_dic
ta2_dic = instructor.ta2_dic
work_dic = grading.work_dic
policies_dic = policies.policies_dic

# variables

semester = 'Spring 2024'
omit_breakdown = True
course_full_dic = {125:'CSDS125',
                   225:'DS225',
                   253:'CS253',
                   377:'CSDS377',
                   387:'CS387'}


for course in [125,253]:

    # create html
    session, year = semester.split()
    course_full = course_full_dic[course]
    output_file = f'archive/{year}_{session}_{course_full}.html'

    content = [
        ('Instructor Information', instructor_dic, 'bulleted_list'),
        ('Teaching Assistant Information', ta1_dic, 'bulleted_list'),
        ('Teaching Assistant Information', ta2_dic, 'bulleted_list'),
        ('Course Information', course_dic[course], None),
        ('Course Work and Grading', work_dic, None),
        ('Course Policies', policies_dic, None)
    ]

    # use template, output html

    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_or_select_template('templates/template1.html')

    output = template.render(course_info = course_dic[course],
                             instructor_info = instructor_dic,
                             body_content = content,
                             semester = semester,
                             omit_breakdown = omit_breakdown)

    with open(output_file, 'w', encoding="utf-8") as fp:
        fp.write(output)

