from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from extractors.makecsv import save_to_file

keyword = input("어떤 직업을 알아보실라우? ")
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword,jobs)