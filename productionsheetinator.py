import sys
import pandas

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

url = sys.argv[1]
template = sys.argv[2]

if "edit" in url:
    url = url.replace("edit", "export?format=tsv&")

eprint("Downloading sheet from url", url)
sheet_data = pandas.read_csv(url, sep='\t')
eprint(sheet_data)

with open("output.tex", 'w') as out:
    with open(template, 'r') as f:
        out.write(f.read() + '\n')

    for _ in sheet_data.iterrows():
        row = _[1]
        out.write('\section{' + row["Step"] + '}\n')
        out.write('\n')
        out.write(row["Description"] + '\n')
        out.write('\n')
    
    out.write('\end{document}\n')
    
