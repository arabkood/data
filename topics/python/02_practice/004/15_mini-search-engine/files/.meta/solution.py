from collections import defaultdict


class SearchEngine:
    def __init__(self):
        self.index = defaultdict(set)
        self.documents = {}

    def add_document(self, doc_id, text):
        self.documents[doc_id] = text
        words = text.lower().split()
        for word in words:
            self.index[word].add(doc_id)

    def search(self, query):
        query_words = query.lower().split()
        if not query_words:
            return []

        # Get documents containing all query words
        doc_scores = defaultdict(int)
        for word in query_words:
            if word in self.index:
                for doc_id in self.index[word]:
                    doc_scores[doc_id] += 1

        # Filter documents that contain all query words
        result = [doc_id for doc_id, score in doc_scores.items() if score == len(query_words)]

        # Sort by score (number of word occurrences)
        result.sort(key=lambda x: (doc_scores[x], -x), reverse=True)

        return result

    def remove_document(self, doc_id):
        if doc_id in self.documents:
            text = self.documents[doc_id]
            words = text.lower().split()
            for word in words:
                self.index[word].discard(doc_id)
            del self.documents[doc_id]
