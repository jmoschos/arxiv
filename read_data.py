import arxiv
from utils import convert_to_dataframe
from config import config


class DataReader:
    def __init__(self, query, sort_by=arxiv.SortCriterion.SubmittedDate):
        self.query = query
        self.max_results = config['max_results']
        self.sort_by = sort_by

    def query_arxiv(self):
        return arxiv.Search(query=self.query, max_results=self.max_results, sort_by=self.sort_by)

    def append_results(self):
        self.papers = []
        for result in self.search.results():
            self.papers.append({
                'published': result.published,
                'title': result.title,
                'abstract': result.summary,
                'categories': result.categories
            })

    def create_dataset(self):
        self.search = self.query_arxiv()
        self.append_results()
        self.output = convert_to_dataframe(self.papers)
        return self.output
