import subprocess


token = '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'
git_url = 'github.com/huojiayang/github.git'
cmd = "cd /Users/zhongfener/Desktop/python/pythonProject"
returned_value = subprocess.call(cmd, shell=True)

cmd = 'git init'
subprocess.call(cmd, shell=True)

cmd = "git add ."
subprocess.call(cmd, shell=True)



cmd = 'git commit -m "111111111"'
subprocess.call(cmd, shell=True)

cmd = 'git remote remove origin'
subprocess.call(cmd, shell=True)

print(665555)
cmd = "git remote add origin https://{}@{}".format(token, git_url)
subprocess.call(cmd, shell=True)
print(222)
cmd = "git push -u origin master -f"
subprocess.call(cmd, shell=True)

print(cmd, 66666)