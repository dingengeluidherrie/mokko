
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
js_file = os.path.join(THIS_FOLDER, 'inputPoncho.js')


# os.chdir(os.getcwd())

def ding(lines):


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


  result_array = [s.split(':') for s in result if len(s.split(':')) == 2]
  result_dict = {e[0].replace("?", ""):e[1].strip() for e in result_array}
  return result_dict