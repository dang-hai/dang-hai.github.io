import re
import shutil
from pathlib import Path
from html5print import HTMLBeautifier

def parse_publications():
    pubs = [pub_dir for pub_dir in Path('./publications').iterdir() if pub_dir.is_dir()]

    for p in pubs:
        index_html = (p / "index.html").read_text().replace("\n", "")
        content = re.findall('<main>(.+)</main>', index_html)[0]
        match = re.search('src="(.+?)"', content)

        for f in p.iterdir():
            if f.suffix.lower() in [".png", ".jpg", ".jpeg"]:
                shutil.copy(f.resolve(), "./docs/images/")

        for m in match.groups():
            start, end = match.span()
            content = f"images/{m}".join([content[:start+5], content[end-1:]])
        # extract main tag
        yield content


if __name__ == "__main__":
    index_template = Path('_index.html').read_text()

    publications = "\n".join([c for c in parse_publications()])

    match = re.search('{(.*)}', index_template)
    start, end = match.span()
    section = match.groups()[0].strip()
    index_template = publications.join([index_template[:start], index_template[end:]])

    with Path('./docs/index.html').open('w') as out:
        html = HTMLBeautifier.beautify(index_template, encoding="utf-8")
        out.write(html)