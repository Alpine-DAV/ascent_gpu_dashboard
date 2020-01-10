import os

def red(text):
  res = '<span style=\"color:red\">' + text +'</span>'
  return res

def green(text):
  res = '<span style=\"color:green\">' + text +'</span>'
  return res

build_dir = './builds'
builds = [dI for dI in os.listdir(build_dir) if os.path.isdir(os.path.join(build_dir,dI))]
builds.sort(reverse=True)
print builds

max_size = 10

num_builds = min(len(builds), max_size)
print num_builds

build_results = []

for i in range(0, num_builds):
  print builds[i]
  report_file = build_dir + '/' + builds[i] + '/report.txt'
  report = open(report_file, 'r')
  build_results.append(report.readline().strip('\n'))
  report.close()

print(build_results)

readme = open("README.md","w")

readme.write("# Lassen Builds Results\n\n")
for i in range(0, num_builds):
  text = ""
  if build_results[i] == 'success':
    text = green('success')
  elif build_results[i] == 'failure':
    text = red('failed')
  else:
    print "no match"

  result = ' - ' + builds[i] + ' : ' + text + '\n'
  readme.write(result)

readme.close()

