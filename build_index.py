import re
import sys
import subprocess

from html5print import HTMLBeautifier
from pathlib import Path

res_edu = subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "notebooks/education.ipynb", "--inplace"])
print("Creating education section exited with: %d" % res_edu.returncode)

res_prof = subprocess.run(["jupyter", "nbconvert", "--to", "notebooks", "--execute", "notebooks/professional.ipynb", "--inplace"])
print("Creating professional section exited with: %d" % res_prof.returncode)

if (res_edu.returncode != 0 or res_prof.returncode != 0):
    print("There was an error during the build. Exit now ...")
    sys.exit()


f = Path(r'_index.html').read_text()
index_html = f

out_path = './public/index.html'

match = re.search('{(.*)}', index_html)
while match:
    start, end = match.span()
    section = match.groups()[0].strip()


    with Path(section).open('r') as _sec:
        index_html = _sec.read().join([index_html[:start], index_html[end:]])
    
    match = re.search('{(.*)}', index_html)


print("Writing index.html to", out_path) 
with Path(out_path).open('w') as out:
    html = HTMLBeautifier.beautify(index_html, 2)
    out.write(html)

print("Done")