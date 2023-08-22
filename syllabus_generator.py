from jinja2 import Environment, FileSystemLoader
# import importlib
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
work_dic = grading.work_dic
policies_dic = policies.policies_dic

# variables
course = 377
semester = 'Fall 2023'
omit_breakdown = True
course_full_dic = {125:'CSDS125',
                   225:'DS225',
                   377:'CSDS377',
                   387:'CS387'}


# create html
session, year = semester.split()
course_full = course_dic[course]
output_file = f'archive/{year}_{session}_{course_full}.html'

content = [
    ('Instructor Information', instructor_dic, 'bulleted_list'),
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

with open(output_file, 'w') as fp:
    fp.write(output)

