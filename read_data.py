import arxiv
import pandas as pd

class DataReader:
    def __init__(self, query, max_results=30, sort_by=arxiv.SortCriterion.SubmittedDate):
        self.query = query
        self.max_results = max_results
        self.sort_by = sort_by

    def query_arxiv(self):
        return arxiv.Search(query=self.query, max_results=self.max_results, sort_by=self.sort_by)

    def append_results(self):
        self.papers = []
        for result in self.search:
            self.papers.append({
                'published': result.published,
                'title': result.title,
                'abstract': result.summary,
                'categories': result.categories
            })

    def create_dataset(self):
        self.search = self.query_arxiv()
        self.append_results()
