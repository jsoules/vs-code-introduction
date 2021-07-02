from typing import List, Union


class MarkdownParser:
    """Parse markdown text to extract code snippets
    """
    def __init__(self, markdown: str) -> None:
        """Constructor for markdown processor

        Args:
            markdown (str): The markdown code
        """
        self._markdown = markdown
        self._lines = markdown.split('\n')
        self._code_snippets: List[CodeSnippet] = []

        current_snippet: Union[List[str], None] = None
        current_language: Union[str, None] = None
        for line in self._lines:
            if current_language is None:
                if line.startswith("```"):
                    current_language = line[3:]
                    current_snippet = []
            else:
                if current_snippet is None:
                    raise Exception('Unexpected, current_snippet is None')
                if line.startswith("```"):
                    self._code_snippets.append(
                        CodeSnippet(
                            language=current_language,
                            code='\n'.join(current_snippet)
                        )
                    )
                    current_snippet = None
                    current_language = None
                else:
                    current_snippet.append(line)
    @property
    def code_snippets(self):
        """Get the extracted code snippets

        Returns:
            List of code snippets
        """
        return [cs for cs in self._code_snippets]

class CodeSnippet:
    def __init__(self, *, language: str, code: str) -> None:
        self._language = language
        self._code = code
    @property
    def language(self):
        return self._language
    @property
    def code(self):
        return self._code