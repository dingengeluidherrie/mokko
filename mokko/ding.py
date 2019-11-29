
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
js_file = os.path.join(THIS_FOLDER, 'inputPoncho.js')


# os.chdir(os.getcwd())

lines = list(open(js_file, 'r'))


for line in lines:
  if(line.startswith('type Props')):
    break
  else:
    lines=lines[1:]

result = []

for line in lines[1:]:
  if(line.startswith('};')):
    break
  elif'/**' not in line:
    result += [line.strip()[:-1]]

result_dict = dict(s.split(':') for s in result)

result_dict = { k:v.strip() for k, v in result_dict.items()}
print(result_dict)