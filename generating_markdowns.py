def generate_markdowns(markdown, text, url_or_language):
    if markdown == 'link':
      return f"[{text}]({url_or_language})"
    if markdown == 'img':
      return f"![{text}]({url_or_language})"
    if markdown == 'code':
      return f"```{url_or_language}\n{text}\n```"

TESTS_LINKS = [
    ('hyperlink', 'https://en.wikipedia.org/wiki/Hyperlink', '[hyperlink](https://en.wikipedia.org/wiki/Hyperlink)'),
    ('Google Search', 'https://www.google.com.au/?safe=active', '[Google Search](https://www.google.com.au/?safe=active)'),
    ('Bing', 'https://www.bing.com/', '[Bing](https://www.bing.com/)'),
    ('Codewars Kata', 'https://www.codewars.com/kata', '[Codewars Kata](https://www.codewars.com/kata)'),
    ('Codewars Dashboard', 'https://www.codewars.com/dashboard', '[Codewars Dashboard](https://www.codewars.com/dashboard)'),
    ('Codewars Dashboard', 'codewars/dashboard', '[Codewars Dashboard](codewars/dashboard)'),
    ('Codewars on Github', 'https://www.github/codewars', '[Codewars on Github](https://www.github/codewars)'),
    ('Codewars Kumite', 'https://www.codewars.com/kumite', '[Codewars Kumite](https://www.codewars.com/kumite)'),
]

TEST_IMG = [
    ('this should be a picture','https://github.com/codewars/gna.jpg','![this should be a picture](https://github.com/codewars/gna.jpg)',)
]

TEST_CODE = [
    ('''def generate_markdowns(markdown, text, url_or_language):
    # Your code here!
    pass''', 'python', "```python\ndef generate_markdowns(markdown, text, url_or_language):\n    # Your code here!\n    pass\n```"),
]

import codewars_test as test

@test.describe('Sample Tests')
def sample():
    
    @test.it("Link markdowns")
    def _():
        for txt,url,exp in TESTS_LINKS:
            test.assert_equals(generate_markdowns('link',txt,url), exp)
    
    @test.it("Image markdowns")
    def _():
        for txt,url,exp in TEST_IMG:
            test.assert_equals(generate_markdowns('img',txt,url), exp)
    
    @test.it("Codeblock markdowns")
    def _():
        for txt,url,exp in TEST_CODE:
            test.assert_equals(generate_markdowns('code',txt,url), exp)
    