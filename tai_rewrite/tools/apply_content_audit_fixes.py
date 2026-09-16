from pathlib import Path
import re

main_path = Path('tai_rewrite/main.tex')
text = main_path.read_text(encoding='utf-8')

# Preserve spaces after the CCG macro in prose.
if '\\usepackage{xspace}' not in text:
    text = text.replace('\\usepackage{enumitem}\n', '\\usepackage{enumitem}\n\\usepackage{xspace}\n\\usepackage{placeins}\n', 1)
text = text.replace('\\newcommand{\\CCG}{\\textsc{CCG}}', '\\newcommand{\\CCG}{\\textsc{CCG}\\xspace}', 1)

# Constrain load-bearing tables to their intended column/page width.
def resize_table(src: str, label: str, width: str) -> str:
    pat = re.compile(
        r'(\\label\{' + re.escape(label) + r'\}.*?)(\\begin\{tabular\}.*?\\end\{tabular\})',
        re.S,
    )
    m = pat.search(src)
    if not m:
        raise RuntimeError(f'Table {label} not found')
    if '\\resizebox' in m.group(0):
        return src
    repl = m.group(1) + f'\\resizebox{{{width}}}{{!}}{{%\n' + m.group(2) + '\n}%'
    return src[:m.start()] + repl + src[m.end():]

for label in ['tab:a1_control', 'tab:proposal_diag', 'tab:candidate_quality', 'tab:intervention']:
    text = resize_table(text, label, '\\columnwidth')
text = resize_table(text, 'tab:main_results', '\\textwidth')

# Prevent the qualitative figure from drifting behind Discussion/References.
marker = '\\section{Discussion}\n'
if '\\FloatBarrier\n\\section{Discussion}' not in text:
    if marker not in text:
        raise RuntimeError('Discussion marker not found')
    text = text.replace(marker, '\\FloatBarrier\n' + marker, 1)

main_path.write_text(text, encoding='utf-8')

supp_path = Path('tai_rewrite/supplementary.tex')
supp = supp_path.read_text(encoding='utf-8')

# Fit the wide SMIYC table to the text block and use a valid float placement.
supp = supp.replace('\\begin{table*}[h]\n\\centering\n\\caption{Existing SMIYC public-validation results.}',
                    '\\begin{table*}[t]\n\\centering\n\\caption{Existing SMIYC public-validation results.}', 1)
smiyc_pat = re.compile(
    r'(\\caption\{Existing SMIYC public-validation results\.\}.*?\\footnotesize\n)(\\begin\{tabular\}.*?\\end\{tabular\})',
    re.S,
)
m = smiyc_pat.search(supp)
if not m:
    raise RuntimeError('SMIYC table not found')
if '\\resizebox' not in m.group(0):
    repl = m.group(1) + '\\resizebox{\\textwidth}{!}{%\n' + m.group(2) + '\n}%'
    supp = supp[:m.start()] + repl + supp[m.end():]

# The supplement contains no citations; remove the empty bibliography robustly.
supp = re.sub(
    r'\n\\bibliographystyle\{IEEEtran\}\n\\bibliography\{\.\./saseg_paper/references,references_additions\}\n',
    '\n',
    supp,
    count=1,
)

supp_path.write_text(supp, encoding='utf-8')
print('Applied final LaTeX layout fixes.')
