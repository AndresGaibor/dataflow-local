---
source: https://qlik.dev/changelog/181-api-updates-assistants-knowledgebases-search/
last_updated: 2025-11-20T16:51:44+01:00
---

# Updated APIs - Assistants and Knowledgebases APIs add search endpoints

The [Assistants API](https://qlik.dev/apis/rest/assistants/) and [Knowledgebases API](https://qlik.dev/apis/rest/knowledgebases/) now let you search
across assistant and knowledge base content using semantic and hybrid search.

The following new endpoints enable this functionality:

- `POST /api/v1/assistants/{assistantId}/search` - Perform search on an assistant using either `SIMPLE`
  (semantic search) or `FULL` mode (semantic search with reranking and hybrid search).
- `POST /api/v1/knowledgebases/{id}/search` - Search chunks from a knowledge base using either `SIMPLE`
  (semantic search) or `FULL` mode (semantic search with reranking and keyword-based search).

Use these endpoints to power intelligent search and content discovery features in your applications.

For more information, refer to:

- [Assistants API reference documentation](https://qlik.dev/apis/rest/assistants/)
- [Knowledgebases API reference documentation](https://qlik.dev/apis/rest/knowledgebases/)
